from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
import gettext


def localeInit():
	gettext.bindtextdomain("MediaInfo", resolveFilename(SCOPE_PLUGINS, "Extensions/MediaInfo/locale"))


def _(txt):
	t = gettext.dgettext("MediaInfo", txt)
	if t == txt:
		#print("[MediaInfo] fallback to default translation for", txt)
		t = gettext.gettext(txt)
	return t


localeInit()
language.addCallback(localeInit)
