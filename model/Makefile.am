#
# Project Ginger
#
# Copyright IBM Corp, 2016
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

models_PYTHON = $(filter-out config.py, $(wildcard *.py))

nodist_models_PYTHON = config.py

EXTRA_DIST = config.py.in

modelsdir = $(pythondir)/wok/plugins/ginger/model

do_substitution = \
	sed -e 's,[@]gingerversion[@],$(PACKAGE_VERSION),g' \
	-e 's,[@]gingerrelease[@],$(PACKAGE_RELEASE),g'

config.py: config.py.in Makefile
	$(do_substitution) < $(srcdir)/config.py.in > config.py

BUILT_SOURCES = config.py
CLEANFILES = config.py \
	$(models_PYTHON:%.py=%.pyc) \
	$(NULL)
