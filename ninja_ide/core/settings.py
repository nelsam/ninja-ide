# -*- coding: utf-8 -*-
#
# This file is part of NINJA-IDE (http://ninja-ide.org).
#
# NINJA-IDE is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# NINJA-IDE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NINJA-IDE; If not, see <http://www.gnu.org/licenses/>.

import os
import sys

from PyQt4.QtGui import QFont
from PyQt4.QtCore import QSettings
from PyQt4.QtCore import QDir
from PyQt4.QtCore import QFileInfo

from ninja_ide import resources
from ninja_ide.dependencies import pep8mod


###############################################################################
# OS DETECTOR
###############################################################################

# Use this flags instead of sys.platform spreaded in the source code
IS_WINDOWS = False
IS_MAC_OS = False

OS_KEY = "Ctrl"

FONT = QFont('Monospace', 12)
if sys.platform == "darwin":
    from PyQt4.QtGui import QKeySequence
    from PyQt4.QtCore import Qt

    FONT = QFont('Monaco', 12)
    OS_KEY = QKeySequence(Qt.CTRL).toString(QKeySequence.NativeText)
    IS_MAC_OS = True
elif sys.platform == "win32":
    FONT = QFont('Courier', 12)
    IS_WINDOWS = True


def detect_python_path():
    if (IS_WINDOWS and PYTHON_EXEC_CONFIGURED_BY_USER) or not IS_WINDOWS:
        return []

    suggested = []
    try:
        drives = [QDir.toNativeSeparators(d.absolutePath())
                  for d in QDir.drives()]
        dirs = []
        for drive in drives:
            info = QFileInfo(drive)
            if info.isReadable():
                dirs += [os.path.join(drive, folder)
                         for folder in os.listdir(drive)]
        for folder in dirs:
            file_path = os.path.join(folder, "python.exe")
            if ("Python" in folder) and os.path.exists(file_path):
                suggested.append(file_path)
    except:
        print("Detection couldnt be executed")

    return suggested

###############################################################################
# IDE
###############################################################################

MAX_OPACITY = 1
MIN_OPACITY = 0.3

TOOLBAR_AREA = 1
#UI LAYOUT
#001 : Central Rotate
#010 : Panels Rotate
#100 : Central Orientation
UI_LAYOUT = 0

LANGUAGE = ""

SHOW_START_PAGE = True

CONFIRM_EXIT = True
HIDE_TOOLBAR = False
SHOW_STATUS_NOTIFICATIONS = True

PYTHON_EXEC = "python"
PYTHON_EXEC_CONFIGURED_BY_USER = False
EXECUTION_OPTIONS = ""

SESSIONS = {}

TOOLBAR_ITEMS = [
    "_MainContainer.show_selector",
    "_MainContainer.add_editor",
    #"ProjectTreeColumn.create_new_project",
    "_MainContainer.open_file",
    "ProjectTreeColumn.open_project_folder",
    "_MainContainer.save_file",
    "_MainContainer.split_vertically",
    "_MainContainer.split_horizontally",
    "IDE.activate_profile",
    "IDE.deactivate_profile",
    #TODO: sessions
    "_MainContainer.editor_cut",
    "_MainContainer.editor_copy",
    "_MainContainer.editor_paste",
    "_ToolsDock.execute_file",
    "_ToolsDock.execute_project",
    "_ToolsDock.kill_application",
    #"run-project", "run-file", "stop", "separator",
    ]

TOOLBAR_ITEMS_DEFAULT = [
    "_MainContainer.show_selector",
    "_MainContainer.add_editor",
    #"ProjectTreeColumn.create_new_project",
    "_MainContainer.open_file",
    "ProjectTreeColumn.open_project_folder",
    "_MainContainer.save_file",
    "_MainContainer.split_assistance",
    #TODO: sessions
    "_MainContainer.editor_cut",
    "_MainContainer.editor_copy",
    "_MainContainer.editor_paste",
    "_ToolsDock.execute_file",
    "_ToolsDock.execute_project",
    "_ToolsDock.kill_application",
    #"run-project", "run-file", "stop", "separator",
    ]

#hold the toolbar actions added by plugins
TOOLBAR_ITEMS_PLUGINS = []

NINJA_SKIN = 'Default'

LAST_OPENED_FILES = []

NOTIFICATION_POSITION = 0


###############################################################################
# EDITOR
###############################################################################

USE_TABS = False
ALLOW_WORD_WRAP = False
INDENT = 4
# by default Unix (\n) is used
USE_PLATFORM_END_OF_LINE = False
MARGIN_LINE = 80
SHOW_MARGIN_LINE = True
REMOVE_TRAILING_SPACES = True
SHOW_TABS_AND_SPACES = True

BRACES = {'{': '}',
    '[': ']',
    '(': ')'}
QUOTES = {'"': '"',
    "'": "'"}

FONT_MAX_SIZE = 28
FONT_MIN_SIZE = 6
MAX_REMEMBER_TABS = 50
COPY_HISTORY_BUFFER = 20

FIND_ERRORS = True
ERRORS_HIGHLIGHT_LINE = True
CHECK_STYLE = True
CHECK_HIGHLIGHT_LINE = True
CODE_COMPLETION = True
COMPLETE_DECLARATIONS = True
SHOW_MIGRATION_TIPS = True
VALID_2TO3 = True
UNDERLINE_NOT_BACKGROUND = True

CENTER_ON_SCROLL = True

SYNTAX = {}

EXTENSIONS = {}

BREAKPOINTS = {}
BOOKMARKS = {}


###############################################################################
# CHECKERS
###############################################################################

CHECK_FOR_DOCSTRINGS = True


###############################################################################
# MINIMAP
###############################################################################

SHOW_MINIMAP = False
MINIMAP_MAX_OPACITY = 0.8
MINIMAP_MIN_OPACITY = 0.1
SIZE_PROPORTION = 0.17


###############################################################################
# FILE MANAGER
###############################################################################

SUPPORTED_EXTENSIONS = [
    '.py',
    '.html',
    '.jpg',
    '.png',
    '.ui',
    '.css',
    '.json',
    '.js',
    '.ini']


###############################################################################
# PROJECTS DATA
###############################################################################

#PROJECT_TYPES = {'Python': None}
PROJECT_TYPES = {}

LANGS = []


###############################################################################
# EXPLORER
###############################################################################

SHOW_PROJECT_EXPLORER = True
SHOW_SYMBOLS_LIST = True
SHOW_WEB_INSPECTOR = False
SHOW_ERRORS_LIST = True
SHOW_MIGRATION_LIST = True

#Backward compatibility with older Qt versions
WEBINSPECTOR_SUPPORTED = True


###############################################################################
# WORKSPACE
###############################################################################

WORKSPACE = ""


###############################################################################
# FUNCTIONS
###############################################################################


def set_project_type_handler(project_type, project_type_handler):
    """
    Set a project type handler for the given project_type
    """
    global PROJECT_TYPES
    PROJECT_TYPES[project_type] = project_type_handler


def get_project_type_handler(project_type):
    """
    Returns the handler for the given project_type
    """
    global PROJECT_TYPES
    return PROJECT_TYPES.get(project_type)


def get_all_project_types():
    """
    Returns the availables project types
    """
    global PROJECT_TYPES
    return list(PROJECT_TYPES.keys())


def add_toolbar_item_for_plugins(toolbar_action):
    """
    Add a toolbar action set from some plugin
    """
    global TOOLBAR_ITEMS_PLUGINS
    TOOLBAR_ITEMS_PLUGINS.append(toolbar_action)


def get_toolbar_item_for_plugins():
    """
    Returns the toolbar actions set by plugins
    """
    global TOOLBAR_ITEMS_PLUGINS
    return TOOLBAR_ITEMS_PLUGINS


def use_platform_specific_eol():
    global USE_PLATFORM_END_OF_LINE
    return USE_PLATFORM_END_OF_LINE

###############################################################################
# Utility functions to update (patch at runtime) pep8mod.py
###############################################################################


def pep8mod_refresh_checks():
    """
    Force to reload all checks in pep8mod.py
    """
    pep8mod.refresh_checks()


def pep8mod_add_ignore(ignore_code):
    """
    Patch pep8mod.py to ignore a given check by code
    EXAMPLE:
        pep8mod_add_ignore('W191')
        'W1919': 'indentation contains tabs'
    """
    pep8mod.options.ignore.append(ignore_code)


def pep8mod_remove_ignore(ignore_code):
    """
    Patch pep8mod.py to remove the ignore of a give check
    EXAMPLE:
        pep8mod_remove_ignore('W191')
        'W1919': 'indentation contains tabs'
    """
    if ignore_code in pep8mod.options.ignore:
        pep8mod.options.ignore.remove(ignore_code)


def pep8mod_update_margin_line_length(new_margin_line):
    """
    Patch pep8mod.py to update the margin line length with a new value
    """
    pep8mod.MAX_LINE_LENGTH = new_margin_line
    pep8mod.options.max_line_length = new_margin_line

###############################################################################
# LOAD SETTINGS
###############################################################################


def load_settings():
    qsettings = QSettings(resources.SETTINGS_PATH, QSettings.IniFormat)
    data_qsettings = QSettings(resources.DATA_SETTINGS_PATH,
        QSettings.IniFormat)
    #Globals
    global TOOLBAR_AREA
    global LANGUAGE
    global SHOW_START_PAGE
    global CONFIRM_EXIT
    global UI_LAYOUT
    global PYTHON_EXEC
    global PYTHON_EXEC_CONFIGURED_BY_USER
    global SESSIONS
    global NINJA_SKIN
    global EXECUTION_OPTIONS
    global SUPPORTED_EXTENSIONS
    global WORKSPACE
    global INDENT
    global USE_PLATFORM_END_OF_LINE
    global MARGIN_LINE
    global REMOVE_TRAILING_SPACES
    global SHOW_TABS_AND_SPACES
    global USE_TABS
    global ALLOW_WORD_WRAP
    global COMPLETE_DECLARATIONS
    global UNDERLINE_NOT_BACKGROUND
    global FONT
    global SHOW_MARGIN_LINE
    global FIND_ERRORS
    global ERRORS_HIGHLIGHT_LINE
    global CHECK_STYLE
    global CHECK_HIGHLIGHT_LINE
    global SHOW_MIGRATION_TIPS
    global CODE_COMPLETION
    global CENTER_ON_SCROLL
    global SHOW_PROJECT_EXPLORER
    global SHOW_SYMBOLS_LIST
    global SHOW_WEB_INSPECTOR
    global SHOW_ERRORS_LIST
    global SHOW_MIGRATION_LIST
    global BOOKMARKS
    global CHECK_FOR_DOCSTRINGS
    global BREAKPOINTS
    global BRACES
    global HIDE_TOOLBAR
    global SHOW_STATUS_NOTIFICATIONS
    global TOOLBAR_ITEMS
    global SHOW_MINIMAP
    global MINIMAP_MAX_OPACITY
    global MINIMAP_MIN_OPACITY
    global SIZE_PROPORTION
    global NOTIFICATION_POSITION
    #General
    HIDE_TOOLBAR = qsettings.value("window/hide_toolbar", False, type=bool)
    SHOW_STATUS_NOTIFICATIONS = qsettings.value(
        "preferences/interface/showStatusNotifications", True, type=bool)
    TOOLBAR_AREA = qsettings.value('preferences/general/toolbarArea', 1,
        type=int)
    LANGUAGE = qsettings.value('preferences/interface/language', '',
        type='QString')
    SHOW_START_PAGE = qsettings.value(
        'preferences/general/showStartPage', True, type=bool)
    CONFIRM_EXIT = qsettings.value('preferences/general/confirmExit',
        True, type=bool)
    UI_LAYOUT = qsettings.value('preferences/interface/uiLayout', 0, type=int)
    PYTHON_EXEC = qsettings.value('preferences/execution/pythonExec',
        'python', type='QString')
    PYTHON_EXEC_CONFIGURED_BY_USER = qsettings.value(
        'preferences/execution/pythonExecConfigured', False, type=bool)
    NINJA_SKIN = qsettings.value('preferences/theme/skin',
        'Default', type='QString')
    sessionDict = dict(data_qsettings.value('ide/sessions', {}))
    for key in sessionDict:
        session_list = list(sessionDict[key])
        files = []
        if session_list:
            files = [item for item in list(session_list[0])]
        tempFiles = []
        for file_ in files:
            fileData = list(file_)
            if len(fileData) > 0:
                tempFiles.append([fileData[0], int(fileData[1]), fileData[2]])
        files = tempFiles
        projects = []
        if len(session_list) > 1:
            projects = [item for item in list(session_list[1])]
        SESSIONS[key] = [files, projects]
    #TODO
    #toolbar_items = [item for item in list(qsettings.value(
        #'preferences/interface/toolbar', []))]
    #if toolbar_items:
        #TOOLBAR_ITEMS = toolbar_items
    #EXECUTION OPTIONS
    EXECUTION_OPTIONS = qsettings.value(
        'preferences/execution/executionOptions',
        defaultValue='', type='QString')
    extensions = [item for item in list(qsettings.value(
        'preferences/general/supportedExtensions', []))]
    if extensions:
        SUPPORTED_EXTENSIONS = extensions
    WORKSPACE = qsettings.value(
        'preferences/general/workspace', "", type='QString')
    #Editor
    SHOW_MINIMAP = qsettings.value(
        'preferences/editor/minimapShow', False, type=bool)
    MINIMAP_MAX_OPACITY = float(qsettings.value(
        'preferences/editor/minimapMaxOpacity', 0.8, type=float))
    MINIMAP_MIN_OPACITY = float(qsettings.value(
        'preferences/editor/minimapMinOpacity', 0.1, type=float))
    SIZE_PROPORTION = float(qsettings.value(
        'preferences/editor/minimapSizeProportion', 0.17, type=float))
    INDENT = int(qsettings.value('preferences/editor/indent', 4, type=int))

    USE_PLATFORM_END_OF_LINE = qsettings.value(
        'preferences/editor/platformEndOfLine', False, type=bool)
    MARGIN_LINE = qsettings.value('preferences/editor/marginLine', 80,
        type=int)
    pep8mod_update_margin_line_length(MARGIN_LINE)
    REMOVE_TRAILING_SPACES = qsettings.value(
        'preferences/editor/removeTrailingSpaces', True, type=bool)
    SHOW_TABS_AND_SPACES = qsettings.value(
        'preferences/editor/showTabsAndSpaces', True, type=bool)
    USE_TABS = qsettings.value('preferences/editor/useTabs', False, type=bool)
    if USE_TABS:
        pep8mod_add_ignore("W191")
        pep8mod_refresh_checks()
    ALLOW_WORD_WRAP = qsettings.value(
        'preferences/editor/allowWordWrap', False, type=bool)
    COMPLETE_DECLARATIONS = qsettings.value(
        'preferences/editor/completeDeclarations', True, type=bool)
    UNDERLINE_NOT_BACKGROUND = qsettings.value(
        'preferences/editor/errorsUnderlineBackground', True, type=bool)
    font = qsettings.value('preferences/editor/font', None)
    if font:
        FONT = font
    SHOW_MARGIN_LINE = qsettings.value(
        'preferences/editor/showMarginLine', True, type=bool)
    FIND_ERRORS = qsettings.value('preferences/editor/errors',
        True, type=bool)
    SHOW_MIGRATION_TIPS = qsettings.value(
        'preferences/editor/showMigrationTips', True, type=bool)
    ERRORS_HIGHLIGHT_LINE = qsettings.value(
        'preferences/editor/errorsInLine', True, type=bool)
    CHECK_STYLE = qsettings.value('preferences/editor/checkStyle',
        True, type=bool)
    CHECK_HIGHLIGHT_LINE = qsettings.value(
        'preferences/editor/checkStyleInline', True, type=bool)
    CODE_COMPLETION = qsettings.value(
        'preferences/editor/codeCompletion', True, type=bool)
    CENTER_ON_SCROLL = qsettings.value(
        'preferences/editor/centerOnScroll', True, type=bool)
    parentheses = qsettings.value('preferences/editor/parentheses', True,
        type=bool)
    if not parentheses:
        del BRACES['(']
    brackets = qsettings.value('preferences/editor/brackets', True, type=bool)
    if not brackets:
        del BRACES['[']
    keys = qsettings.value('preferences/editor/keys', True, type=bool)
    if not keys:
        del BRACES['{']
    simpleQuotes = qsettings.value('preferences/editor/simpleQuotes',
        True, type=bool)
    if not simpleQuotes:
        del QUOTES["'"]
    doubleQuotes = qsettings.value('preferences/editor/doubleQuotes',
        True, type=bool)
    if not doubleQuotes:
        del QUOTES['"']
    #Projects
    SHOW_PROJECT_EXPLORER = qsettings.value(
        'preferences/interface/showProjectExplorer', True, type=bool)
    SHOW_SYMBOLS_LIST = qsettings.value(
        'preferences/interface/showSymbolsList', True, type=bool)
    SHOW_WEB_INSPECTOR = qsettings.value(
        'preferences/interface/showWebInspector', False, type=bool)
    SHOW_ERRORS_LIST = qsettings.value(
        'preferences/interface/showErrorsList', False, type=bool)
    SHOW_MIGRATION_LIST = qsettings.value(
        'preferences/interface/showMigrationList', True, type=bool)
    #Bookmarks and Breakpoints
    bookmarks = dict(qsettings.value('preferences/editor/bookmarks', {}))
    for key in bookmarks:
        if key:
            BOOKMARKS[key] = [int(i) for i in list(bookmarks[key])]
    breakpoints = dict(qsettings.value('preferences/editor/breakpoints', {}))
    for key in breakpoints:
        if key:
            BREAKPOINTS[key] = [int(i) for i in list(breakpoints[key])]
    # Checkers
    CHECK_FOR_DOCSTRINGS = qsettings.value(
        'preferences/editor/checkForDocstrings', False, type=bool)
    NOTIFICATION_POSITION = qsettings.value(
        'preferences/general/notification_position', 0, type=int)
    from ninja_ide.extensions import handlers
    handlers.init_basic_handlers()
