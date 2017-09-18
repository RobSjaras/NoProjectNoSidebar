import sublime
import sublime_plugin

class NoProjectNoSidebarEvents(sublime_plugin.EventListener):
    def on_new(self, view):
        if view.window().project_file_name() == None:
            view.window().set_sidebar_visible(False)
