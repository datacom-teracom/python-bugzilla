import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bugzilla.base import Bugzilla


class DmBugzilla(Bugzilla):
    """
    Class to extend generic Bugzilla class and create a specialization for
    Datacom Bugzilla instance.
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

                     # From here are the Datacom Bugzilla Custom Fields
                     cf_affected_modules=None,
                     cf_dmos_olt_version=None,
                     cf_chamado_datacom=None,
                     cf_is_integrated_on_dmos=None,
                     cf_customer=None,
                     cf_frequency=None,
                     cf_rally_team=None,
                     cf_rally_team_drop=None,
                     cf_rally_synch=None,
                     cf_rally_id=None,
                     cf_rally_url=None,
                     cf_rally_rank=None,
                     cf_rally_iteration=None,
                     cf_bug_impact=None,
                     cf_parent=None,
                     cf_child=None,
                     cf_blocked=None,
                     cf_blocking_reason=None,
                     cf_blocking_details=None,
                     cf_old_bug=None,
                     cf_since=None,
                     cf_why_now=None,
                     cf_target=None,
                     cf_testcase=None,
                     cf_review_id=None,
                     cf_review_url=None,
                     cf_review_state=None,
                     cf_target_dmos_version=None,
                     cf_jenkins_job=None,
                     cf_jenkins_phase=None,
                     cf_jenkins_build=None,
                     cf_jenkins_cause=None,
                     cf_rn_presence=None,
                     cf_rn_category=None,
                     cf_rn_retriction_version=None,
                     cf_rn_details_text=None,
                     cf_rn_ready=None,
                     cf_rn_done=None,
                     cf_yodiz_url=None,
                     cf_rank=None,
                     cf_security_bug=None):
        """
        Extends super().build_update() adding Datacom Bugzilla Custom Fields.
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
        ret = self._add_to_dict(ret, 'cf_affected_modules',
                                cf_affected_modules)
        ret = self._add_to_dict(ret, 'cf_dmos_olt_version',
                                cf_dmos_olt_version)
        ret = self._add_to_dict(ret, 'cf_chamado_datacom',
                                cf_chamado_datacom)
        ret = self._add_to_dict(ret, 'cf_is_integrated_on_dmos',
                                cf_is_integrated_on_dmos)
        ret = self._add_to_dict(ret, 'cf_customer',
                                cf_customer)
        ret = self._add_to_dict(ret, 'cf_frequency',
                                cf_frequency)
        ret = self._add_to_dict(ret, 'cf_rally_team',
                                cf_rally_team)
        ret = self._add_to_dict(ret, 'cf_rally_team_drop',
                                cf_rally_team_drop)
        ret = self._add_to_dict(ret, 'cf_rally_synch',
                                cf_rally_synch)
        ret = self._add_to_dict(ret, 'cf_rally_id',
                                cf_rally_id)
        ret = self._add_to_dict(ret, 'cf_rally_url',
                                cf_rally_url)
        ret = self._add_to_dict(ret, 'cf_rally_rank',
                                cf_rally_rank)
        ret = self._add_to_dict(ret, 'cf_rally_iteration',
                                cf_rally_iteration)
        ret = self._add_to_dict(ret, 'cf_bug_impact',
                                cf_bug_impact)
        ret = self._add_to_dict(ret, 'cf_parent',
                                cf_parent)
        ret = self._add_to_dict(ret, 'cf_child',
                                cf_child)
        ret = self._add_to_dict(ret, 'cf_blocked',
                                cf_blocked)
        ret = self._add_to_dict(ret, 'cf_blocking_reason',
                                cf_blocking_reason)
        ret = self._add_to_dict(ret, 'cf_blocking_details',
                                cf_blocking_details)
        ret = self._add_to_dict(ret, 'cf_old_bug',
                                cf_old_bug)
        ret = self._add_to_dict(ret, 'cf_since',
                                cf_since)
        ret = self._add_to_dict(ret, 'cf_why_now',
                                cf_why_now)
        ret = self._add_to_dict(ret, 'cf_target',
                                cf_target)
        ret = self._add_to_dict(ret, 'cf_testcase',
                                cf_testcase)
        ret = self._add_to_dict(ret, 'cf_review_id',
                                cf_review_id)
        ret = self._add_to_dict(ret, 'cf_review_url',
                                cf_review_url)
        ret = self._add_to_dict(ret, 'cf_review_state',
                                cf_review_state)
        ret = self._add_to_dict(ret, 'cf_target_dmos_version',
                                cf_target_dmos_version)
        ret = self._add_to_dict(ret, 'cf_jenkins_job',
                                cf_jenkins_job)
        ret = self._add_to_dict(ret, 'cf_jenkins_phase',
                                cf_jenkins_phase)
        ret = self._add_to_dict(ret, 'cf_jenkins_build',
                                cf_jenkins_build)
        ret = self._add_to_dict(ret, 'cf_jenkins_cause',
                                cf_jenkins_cause)
        ret = self._add_to_dict(ret, 'cf_rn_presence',
                                cf_rn_presence)
        ret = self._add_to_dict(ret, 'cf_rn_category',
                                cf_rn_category)
        ret = self._add_to_dict(ret, 'cf_rn_retriction_version',
                                cf_rn_retriction_version)
        ret = self._add_to_dict(ret, 'cf_rn_details_text',
                                cf_rn_details_text)
        ret = self._add_to_dict(ret, 'cf_rn_ready',
                                cf_rn_ready)
        ret = self._add_to_dict(ret, 'cf_rn_done',
                                cf_rn_done)
        ret = self._add_to_dict(ret, 'cf_yodiz_url',
                                cf_yodiz_url)
        ret = self._add_to_dict(ret, 'cf_rank',
                                cf_rank)
        ret = self._add_to_dict(ret, 'cf_security_bug',
                                cf_security_bug)

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

                        # From here are the Datacom Bugzilla Custom Fields
                        cf_affected_modules=None,
                        cf_dmos_olt_version=None,
                        cf_chamado_datacom=None,
                        cf_is_integrated_on_dmos=None,
                        cf_customer=None,
                        cf_frequency=None,
                        cf_rally_team=None,
                        cf_rally_team_drop=None,
                        cf_rally_synch=None,
                        cf_rally_id=None,
                        cf_rally_url=None,
                        cf_rally_rank=None,
                        cf_rally_iteration=None,
                        cf_bug_impact=None,
                        cf_parent=None,
                        cf_child=None,
                        cf_blocked=None,
                        cf_blocking_reason=None,
                        cf_blocking_details=None,
                        cf_old_bug=None,
                        cf_since=None,
                        cf_why_now=None,
                        cf_target=None,
                        cf_testcase=None,
                        cf_review_id=None,
                        cf_review_url=None,
                        cf_review_state=None,
                        cf_target_dmos_version=None,
                        cf_jenkins_job=None,
                        cf_jenkins_phase=None,
                        cf_jenkins_build=None,
                        cf_jenkins_cause=None,
                        cf_rn_presence=None,
                        cf_rn_category=None,
                        cf_rn_retriction_version=None,
                        cf_rn_details_text=None,
                        cf_rn_ready=None,
                        cf_rn_done=None,
                        cf_yodiz_url=None,
                        cf_rank=None,
                        cf_security_bug=None):
        """
        Extends super().build_createbug() adding Datacom Bugzilla Custom Fields
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
        ret = self.build_update(cf_affected_modules=cf_affected_modules,
                cf_dmos_olt_version=cf_dmos_olt_version,
                cf_chamado_datacom=cf_chamado_datacom,
                cf_is_integrated_on_dmos=cf_is_integrated_on_dmos,
                cf_customer=cf_customer,
                cf_frequency=cf_frequency,
                cf_rally_team=cf_rally_team,
                cf_rally_team_drop=cf_rally_team_drop,
                cf_rally_synch=cf_rally_synch,
                cf_rally_id=cf_rally_id,
                cf_rally_url=cf_rally_url,
                cf_rally_rank=cf_rally_rank,
                cf_rally_iteration=cf_rally_iteration,
                cf_bug_impact=cf_bug_impact,
                cf_parent=cf_parent,
                cf_child=cf_child,
                cf_blocked=cf_blocked,
                cf_blocking_reason=cf_blocking_reason,
                cf_blocking_details=cf_blocking_details,
                cf_old_bug=cf_old_bug,
                cf_since=cf_since,
                cf_why_now=cf_why_now,
                cf_target=cf_target,
                cf_testcase=cf_testcase,
                cf_review_id=cf_review_id,
                cf_review_url=cf_review_url,
                cf_review_state=cf_review_state,
                cf_target_dmos_version=cf_target_dmos_version,
                cf_jenkins_job=cf_jenkins_job,
                cf_jenkins_phase=cf_jenkins_phase,
                cf_jenkins_build=cf_jenkins_build,
                cf_jenkins_cause=cf_jenkins_cause,
                cf_rn_presence=cf_rn_presence,
                cf_rn_category=cf_rn_category,
                cf_rn_retriction_version=cf_rn_retriction_version,
                cf_rn_details_text=cf_rn_details_text,
                cf_rn_ready=cf_rn_ready,
                cf_rn_done=cf_rn_done,
                cf_yodiz_url=cf_yodiz_url,
                cf_rank=cf_rank,
                cf_security_bug=cf_security_bug)

        return ret
