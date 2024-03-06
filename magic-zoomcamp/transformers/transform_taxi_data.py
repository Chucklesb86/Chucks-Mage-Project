if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print("Rows with zero passengers:", data['passenger_count'].isin([0]).sum())
    print("Rows with zero distance:", data['trip_distance'].isin([0]).sum())
    print("venderid is not missing", 'VendorID' in data.columns)
    data.columns = (data.columns
                     .str.lower()
    )
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]


@test
def test_output(output, *args):
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with no distaince'
    assert 'vendorid' in output.columns, 'vender id is missing'