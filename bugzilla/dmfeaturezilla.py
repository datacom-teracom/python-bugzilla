import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bugzilla.base import Bugzilla


class DmFeaturezilla(Bugzilla):
    """
    Class to extend generic Bugzilla class and create a specialization for
    Datacom Featurezilla instance.
    """

    ###########################################################################


    def _add_to_dict(self, dictionary, field, value):
        """
        Add the given value to the given field in the given dictionary if
        value is not None.

        Return updated dictionary.
        """
        if value is not None:
            dictionary[field] = value

        return dictionary

    ###########################################################################


    def build_update(self,
                     alias=None,
                     assigned_to=None,
                     blocks_add=None,
                     blocks_remove=None,
                     blocks_set=None,
                     depends_on_add=None,
                     depends_on_remove=None,
                     depends_on_set=None,
                     cc_add=None,
                     cc_remove=None,
                     is_cc_accessible=None,
                     comment=None,
                     comment_private=None,
                     component=None,
                     deadline=None,
                     dupe_of=None,
                     estimated_time=None,
                     groups_add=None,
                     groups_remove=None,
                     keywords_add=None,
                     keywords_remove=None,
                     keywords_set=None,
                     op_sys=None,
                     platform=None,
                     priority=None,
                     product=None,
                     qa_contact=None,
                     is_creator_accessible=None,
                     remaining_time=None,
                     reset_assigned_to=None,
                     reset_qa_contact=None,
                     resolution=None,
                     see_also_add=None,
                     see_also_remove=None,
                     severity=None,
                     status=None,
                     summary=None,
                     target_milestone=None,
                     target_release=None,
                     url=None,
                     version=None,
                     whiteboard=None,
                     work_time=None,
                     fixed_in=None,
                     qa_whiteboard=None,
                     devel_whiteboard=None,
                     internal_whiteboard=None,
                     sub_component=None,
                     flags=None,
                     comment_tags=None,
                     minor_update=None,

                     # From here are the Datacom Featurezilla Custom Fields
                     cf_investmentcategory=None,
                     cf_dev_tshirt=None,
                     cf_rank=None,
                     cf_customer_text=None,
                     cf_target_version=None,
                     cf_rally_url=None):
        """
        Extends super().build_update() adding Datacom Featurezilla Custom
        Fields.
        """

        ########################
        # Call original method #
        ########################
        ret = super().build_update(alias,
                             assigned_to,
                             blocks_add,
                             blocks_remove,
                             blocks_set,
                             depends_on_add,
                             depends_on_remove,
                             depends_on_set,
                             cc_add,
                             cc_remove,
                             is_cc_accessible,
                             comment,
                             comment_private,
                             component,
                             deadline,
                             dupe_of,
                             estimated_time,
                             groups_add,
                             groups_remove,
                             keywords_add,
                             keywords_remove,
                             keywords_set,
                             op_sys,
                             platform,
                             priority,
                             product,
                             qa_contact,
                             is_creator_accessible,
                             remaining_time,
                             reset_assigned_to,
                             reset_qa_contact,
                             resolution,
                             see_also_add,
                             see_also_remove,
                             severity,
                             status,
                             summary,
                             target_milestone,
                             target_release,
                             url,
                             version,
                             whiteboard,
                             work_time,
                             fixed_in,
                             qa_whiteboard,
                             devel_whiteboard,
                             internal_whiteboard,
                             sub_component,
                             flags,
                             comment_tags,
                             minor_update)

        ######################################################
        # Increment original return with custom field values #
        ######################################################
        ret = self._add_to_dict(ret, 'cf_investmentcategory',
                                cf_investmentcategory)
        ret = self._add_to_dict(ret, 'cf_dev_tshirt',
                                cf_dev_tshirt)
        ret = self._add_to_dict(ret, 'cf_rank',
                                cf_rank)
        ret = self._add_to_dict(ret, 'cf_customer_text',
                                cf_customer_text)
        ret = self._add_to_dict(ret, 'cf_target_version',
                                cf_target_version)
        ret = self._add_to_dict(ret, 'cf_rally_url',
                                cf_rally_url)

        return ret

    ###########################################################################

    def build_createbug(self,
                        product=None,
                        component=None,
                        version=None,
                        summary=None,
                        description=None,
                        comment_private=None,
                        blocks=None,
                        cc=None,
                        assigned_to=None,
                        keywords=None,
                        depends_on=None,
                        groups=None,
                        op_sys=None,
                        platform=None,
                        priority=None,
                        qa_contact=None,
                        resolution=None,
                        severity=None,
                        status=None,
                        target_milestone=None,
                        target_release=None,
                        url=None,
                        sub_component=None,
                        alias=None,
                        comment_tags=None,

                        # From here are the Datacom Featurezilla Custom Fields
                     cf_investmentcategory=None,
                     cf_dev_tshirt=None,
                     cf_rank=None,
                     cf_customer_text=None,
                     cf_target_version=None,
                     cf_rally_url=None):
        """
        Extends super().build_createbug() adding Datacom Featurezilla Custom
        Fields.
        """

        ########################
        # Call original method #
        ########################
        ret = super().build_createbug(product,
                                      component,
                                      version,
                                      summary,
                                      description,
                                      comment_private,
                                      blocks,
                                      cc,
                                      assigned_to,
                                      keywords,
                                      depends_on,
                                      groups,
                                      op_sys,
                                      platform,
                                      priority,
                                      qa_contact,
                                      resolution,
                                      severity,
                                      status,
                                      target_milestone,
                                      target_release,
                                      url,
                                      sub_component,
                                      alias,
                                      comment_tags)

        ######################################################
        # Increment original return with custom field values #
        ######################################################
        ret = self.build_update(cf_investmentcategory=cf_investmentcategory,
                cf_dev_tshirt=cf_dev_tshirt,
                cf_rank=cf_rank,
                cf_customer_text=cf_customer_text,
                cf_target_version=cf_target_version,
                cf_rally_url=cf_rally_url)

        return ret
