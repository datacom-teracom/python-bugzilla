from bugzilla.dmfeaturezilla import DmFeaturezilla

###############################################################################


def test_build_createbug():
    bz = DmFeaturezilla(url=None)

    # Create empty
    result = bz.build_createbug()
    assert result == {}

    # Create with custom fields
    result = bz.build_createbug(
        cf_investmentcategory='value of cf_investmentcategory',
        cf_dev_tshirt='value of cf_dev_tshirt',
        cf_rank='value of cf_rank',
        cf_customer_text='value of cf_customer_text',
        cf_target_version='value of cf_target_version',
        cf_rally_url='value of cf_rally_url')
    assert result == {
        'cf_investmentcategory': 'value of cf_investmentcategory',
        'cf_dev_tshirt': 'value of cf_dev_tshirt',
        'cf_rank': 'value of cf_rank',
        'cf_customer_text': 'value of cf_customer_text',
        'cf_target_version': 'value of cf_target_version',
        'cf_rally_url': 'value of cf_rally_url',
    }

###############################################################################


def test_build_update():
    bz = DmFeaturezilla(url=None)

    # Create empty
    result = bz.build_update()
    assert result == {}

    # Create with custom fields
    result = bz.build_update(
        cf_investmentcategory='value of cf_investmentcategory',
        cf_dev_tshirt='value of cf_dev_tshirt',
        cf_rank='value of cf_rank',
        cf_customer_text='value of cf_customer_text',
        cf_target_version='value of cf_target_version',
        cf_rally_url='value of cf_rally_url')
    assert result == {
        'cf_investmentcategory': 'value of cf_investmentcategory',
        'cf_dev_tshirt': 'value of cf_dev_tshirt',
        'cf_rank': 'value of cf_rank',
        'cf_customer_text': 'value of cf_customer_text',
        'cf_target_version': 'value of cf_target_version',
        'cf_rally_url': 'value of cf_rally_url',
    }
