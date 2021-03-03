import pytest

from account import Account


@pytest.fixture
def account():
    return Account("John Smith", 1_000)


class TestAccount:
    def test_init_sets_default_starting_balance(self):
        assert Account("").balance == 0

    def test_str(self, account):
        assert str(account) == "Account of John Smith with starting amount: 1000"

    def test_repr(self, account):
        assert repr(account) == "Account('John Smith', 1000)"

    def test_add_transaction_adds_transaction(self, account):
        assert not account._transactions
        account.add_transaction(100)
        assert account._transactions == [100]

    def test_add_transaction_wrong_type_raises_value_error(self, account):
        with pytest.raises(ValueError, match="please use int for amount"):
            account.add_transaction("100")

    def test_balance_getter_calculates_correct_balance(self, account):
        account.add_transaction(100)
        account.add_transaction(-50)
        account.add_transaction(250)
        assert account.balance == 1_300

    def test_ordering(self):
        acc_500 = Account("", 500)
        acc_1000 = Account("", 1_000)
        acc_2000 = Account("", 2_000)

        assert acc_1000 == acc_1000
        assert acc_1000 != acc_2000
        assert not acc_1000 < acc_1000
        assert acc_1000 < acc_2000
        assert acc_1000 > acc_500
        assert not acc_1000 > acc_2000

    def test_add_adds_other_owner_and_transfers_balances(self, account):
        account.add_transaction(100)
        other_account = Account("Jane Smith", 2_000)
        other_account.add_transaction(200)

        joint_account = account + other_account

        assert joint_account.owner == "John Smith&Jane Smith"
        assert joint_account.amount == 3_000
        assert joint_account._transactions == [100, 200]
