#/***************************************************************************
# OmgevingsAnalyse
#
# Maak een rapport over de omgeving van een adres, perceel of punt
#							 -------------------
#		begin				: 2016-03-31
#		git sha				: $Format:%H$
#		copyright			: (C) 2016 by Kay Warrie
#		email				: kaywarrie@gmail.com
# ***************************************************************************/
#
#/***************************************************************************
# *																		 *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or	 *
# *   (at your option) any later version.								   *
# *																		 *
# ***************************************************************************/

#################################################
# Edit the following to match your sources lists
#################################################


#Add iso code for any locales you want to support here (space separated)
# default is no locales
# LOCALES = af
LOCALES =

# If locales are enabled, set the name of the lrelease binary on your system. If
# you have trouble compiling the translations, you may have to specify the full path to
# lrelease
#LRELEASE = lrelease
#LRELEASE = lrelease-qt4


# translation
SOURCES = \
	__init__.py \
	OmgevingsAnalyse.py OmgevingsAnalyse_dialog.py

PLUGINNAME = Omgevings_Analyse_Rapport

PY_FILES = \
	__init__.py  utils.py htmlInteraction.py  \
	OmgevingsAnalyse.py OmgevingsAnalyseDlg.py mapTool.py rapportGenerator.py settings.py

UI_FILES = ui_OmgevingsAnalyseDlg.py ui_resultDlg.py ui_progressBar.py

EXTRAS = metadata.txt img data

RESOURCE_FILES = resources_rc.py

PEP8EXCLUDE=pydev,resources.py,conf.py,third_party,ui


#################################################
# Normally you would not need to edit below here
#################################################

HELP = help/build/html

PLUGIN_UPLOAD = $(c)/scripts/plugin_upload.py

RESOURCE_SRC=$(shell grep '^ *<file' resources.qrc | sed 's@</file>@@g;s/.*>//g' | tr '\n' ' ')

QGISDIR=.qgis2

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES)

%_rc.py : %.qrc
	pyrcc4 -o $*_rc.py  $<

%.py : %.ui
	pyuic4 -o $@ $<

deploy: compile transcompile derase
	# The deploy  target only works on unix like operating system where
	# the Python plugin directory is located at:
	# $HOME/$(QGISDIR)/python/plugins
	if [ -d "$(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)" ]; then rm -r $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME); fi
	mkdir -p $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vfr $(EXTRAS) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vfr i18n $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vf $(UI_FILES) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)

# [KW]: extra command with my own python script, that I can also use on windows
# workflow testPlugin.py: pack -> extract at QGISDIR -> start QGIS
runplugin: compile  
	python $(CURDIR)/scripts/testPlugin.py
	

# The dclean target removes compiled python files from plugin directory
# also deletes any .git entry
dclean:
	find $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME) -iname "*.pyc" -delete
	find $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME) -iname ".git" -prune -exec rm -Rf {} \;

derase:
	if [ -d "$(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME)" ]; then rm -r $(HOME)/$(QGISDIR)/python/plugins/$(PLUGINNAME); fi

zip: deploy
	# The zip target deploys the plugin and creates a zip file with the deployed
	# content. You can then upload the zip file on http://plugins.qgis.org
	rm -f build/$(PLUGINNAME).zip
	cd $(HOME)/$(QGISDIR)/python/plugins; zip -9r $(CURDIR)/build/$(PLUGINNAME).zip $(PLUGINNAME)

package: compile
	# Create a zip package of the plugin named $(PLUGINNAME).zip.
	# This requires use of git (your plugin development directory must be a
	# git repository).
	# To use, pass a valid commit or tag as follows:
	#   make package VERSION=Version_0.3.2
	rm -f $(PLUGINNAME).zip
	git archive --prefix=$(PLUGINNAME)/ -o $(PLUGINNAME).zip $(VERSION)
	echo "Created package: $(PLUGINNAME).zip"

upload: zip
	$(PLUGIN_UPLOAD) $(PLUGINNAME).zip

transup:
	@chmod +x scripts/update-strings.sh
	@scripts/update-strings.sh $(LOCALES)

transcompile:
	@chmod +x scripts/compile-strings.sh
	@scripts/compile-strings.sh lrelease $(LOCALES)

transclean:
	rm -f i18n/*.qm

clean:
	rm $(UI_FILES) $(RESOURCE_FILES)