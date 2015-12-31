#
# Project Ginger
#
# Copyright IBM, Corp. 2015
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

from wok.control.base import Collection, Resource


class SysModules(Collection):
    def __init__(self, model):
        super(SysModules, self).__init__(model)
        self.role_key = 'adminstration'
        self.admin_methods = ['GET', 'POST']
        self.resource = SysModule


class SysModule(Resource):
    def __init__(self, model, ident):
        super(SysModule, self).__init__(model, ident)
        self.role_key = 'administration'
        self.admin_methods = ['GET', 'DELETE']
        self.uri_fmt = "/sysmodules/%s"

    @property
    def data(self):
        return self.info
