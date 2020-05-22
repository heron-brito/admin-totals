# coding=utf-8
from __future__ import division, print_function, unicode_literals

from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
import logging
logger = logging.getLogger(__name__)


'''
class ChangeListTotals(ChangeList):
    def get_results(self, *args, **kwargs):
        super(ChangeListTotals, self).get_results(*args, **kwargs)
        if hasattr(self.model_admin, 'list_totals'):
            self.aggregations = []
            list_totals = dict(self.model_admin.list_totals)
            for field in self.list_display:
                if field in list_totals:
                    self.aggregations.append(
                        self.result_list.aggregate(agg=list_totals[field](field))['agg'])
                else:
                    self.aggregations.append('')

'''
# Heron
class ChangeListTotals(ChangeList):
    logger.warning('on the changelist ')
    def get_results(self, *args, **kwargs):
        super(ChangeListTotals, self).get_results(*args, **kwargs)
        if hasattr(self.model_admin, 'list_totals'):
            logger.warning('has list_totals ' + str(self.model_admin.list_totals))
            self.aggregations = []
            list_totals = dict(self.model_admin.list_totals)
            logger.warning('list_totals: ' + str(list_totals))
            for field in self.list_display:
                logger.warning('filed list_display: ' + str(field))
                if field in list_totals:
                    logger.warning('filed: ' + str(field))
                    logger.warning(self.result_list)
                    self.aggregations.append(
                        self.result_list.aggregate(agg=list_totals[field](field))['agg'])
                    logger.warning('list_totals[field](field))[agg]:')
                    logger.warning(self.aggregations)
                    #logger.warning(list_totals[field](field)['agg'])
                else:
                    self.aggregations.append('')


class ModelAdminTotals(admin.ModelAdmin):
    change_list_template = 'admin_totals/change_list_totals.html'

    def get_changelist(self, request, **kwargs):
        return ChangeListTotals
