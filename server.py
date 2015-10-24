import bottle
import calendar
import os
import datetime


__author__ = 'David Fradis'

PORT = int(os.eniron.get('PORT', 5000))

now = datetime.datetime.now()
cal = calendar.HTMLcalendar()

@bottle.route('/static/<filename>')
def server_static(filename):
  return bottle.static_file(filename, root='./static')

@bottle.route('/')
@bottle.route('/<year>/<month>')
def render_calendar(year=now.year, month=now.month):
  year = int(year)
  month = int(month)

  return bottle.template('calendar', calendar=c.formatmonth(year, month))

  bottle.run(host='0.0.0.0', port=PORT, debug=true)
