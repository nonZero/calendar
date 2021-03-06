import calendar
class SelectableCalendar(calendar.HTMLCalendar):
  def formatday(self, day, weekday):
    """
      Return a day as a table cell.
    """
    if day == 0:
        return '<td class="noday">&nbsp;</td>' # day outside month
    else:
        return '<td class="/%s"><a href="/%s">%d</a></td>' % (self.cssclasses[weekday],day, day)
