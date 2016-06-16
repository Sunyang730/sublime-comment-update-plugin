import sublime
import sublime_plugin
import datetime
import re

class UpdateCommentOnSave(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    # cfg = view.settings().get('update_commnet_on_save', True)

    # path = view.file_name()

    # extension = (path.split('.')[-1]).lower()
    view.run_command('replace')


class ReplaceCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    region = sublime.Region(0, self.view.size())
    substr = self.view.substr(region)
    updated_string = re.sub(r'Copyright \(c\) \d\d\d\d,', 'Copyright (c) ' + str(datetime.date.today().year), substr)
    self.view.replace(edit, region, updated_string)


