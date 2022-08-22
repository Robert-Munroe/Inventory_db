import sys
from helper_functions import entrybuilder

sys.path.insert(0, r'C:\Users\rmunr\PycharmProjects\foundersinventorydatabase\helper_functions')


def test_entry_builder():
    good_fsg_id = '21s0001'
    new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(good_fsg_id)
    assert new_fsg_id == '21S0001'
    good_fsg_id = '21S0001'
    new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(good_fsg_id)
    assert new_fsg_id == '21S0001'
    good_fsg_id = '21r0001'
    new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(good_fsg_id)
    assert new_fsg_id == '21R0001'
    good_fsg_id = '21R0001'
    new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(good_fsg_id)
    assert new_fsg_id == '21R0001'
    bad_fsg_id = ''
    new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(bad_fsg_id)
    assert new_fsg_id is None
    bad_fsg_id = '2222222'
    new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(bad_fsg_id)
    assert new_fsg_id is None
    bad_fsg_id = '21s00000'
    new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(bad_fsg_id)
    assert new_fsg_id is None
    bad_fsg_id = '$$$$$$$$$'
    new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(bad_fsg_id)
    assert new_fsg_id is None
    bad_fsg_id = 'aas0001'
    new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(bad_fsg_id)
    assert new_fsg_id is None
    bad_fsg_id = '22a0001'
    new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(bad_fsg_id)
    assert new_fsg_id is None

    for i in range(10, 100):
        good_fsg_id = str(i) + 's0001'
        new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(good_fsg_id)
        assert new_fsg_id is not None

    for i in range(0, 10):
        good_fsg_id = '0' + str(i) + 's0001'
        new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(good_fsg_id)
        assert new_fsg_id is not None

    for i in range(0, 10):
        good_fsg_id = '21s000' + str(i)
        new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(good_fsg_id)
        assert new_fsg_id is not None

    for i in range(10, 100):
        good_fsg_id = '21s00' + str(i)
        new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(good_fsg_id)
        assert new_fsg_id is not None

    for i in range(100, 1000):
        good_fsg_id = '21s0' + str(i)
        new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(good_fsg_id)
        assert new_fsg_id is not None

    for i in range(1000, 10000):
        good_fsg_id = '21s' + str(i)
        new_fsg_id = entrybuilder.ask_for_fsg_id_allow_duplicate(good_fsg_id)
        assert new_fsg_id is not None
