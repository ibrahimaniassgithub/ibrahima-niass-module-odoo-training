from odoo import models, fields, api
class Session(models.Model):
    _name = 'myacademy.session'
    _description = "MyAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    course_ids = fields.Many2one('openacademy.course',  ondelete='cascade', string="Course", required=True)
    teacher_ids=fields.Many2one('res.partner',domain=[ ('grade', '!=', '')], string="Teacher")
    student_ids=fields.Many2many('res.partner',domain=[ ('age', '!=', 0)], string="List of student")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue
            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            r.duration = (r.end_date - r.start_date).days + 1

    @api.depends('seats', 'student_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.student_ids) / r.seats
    
    @api.onchange('seats', 'student_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(self.student_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }
    
    @api.constrains('teacher_ids', 'student_ids')
    def _check_instructor_not_in_student(self):
        for r in self:
            if r.teacher_ids and r.teacher_ids in r.student_ids:
                raise exceptions.ValidationError("A session's teacher can't be an student")
