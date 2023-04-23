from pyteal import *
from pyteal.ast.bytes import Bytes
from pyteal_helpers import program


def approval():

    local_lab = Bytes("lab")
    local_wager = Bytes("wager")
    local_garden_id= Bytes("garden_id")
    local_veggie_type = Bytes("veggie_type")
    local_veggie_quality = Bytes("veggie_quality")

    op_create = Bytes("create")
    op_accept = Bytes("accept")
    op_resolve = Bytes("resolve")

    return program.event(
        init=Approve(),
        opt_in=Seq(
            reset(Int(0)),
            Approve(),
        ),
        no_op=Seq(
            Cond(
                [Txn.application_args[0] == op_create, create_quality_check()],
                [Txn.application_args[0] == op_accept, accept_quality_check()],
                [Txn.application_args[0] == op_resolve, resolve_quality_check()],
            ),
            Reject(),
        ),
    )

@Subroutine(TealType.none)
def create_quality_check():
    return Seq(
        program.check_self(
            group_size=Int(2),
            group_index=Int (8)

        ),
        program.check_rekey_zero(2),
        Assert(
            And(
                Gtxn[1].type_enum() == TxnType.Payment,
                Gtxn[1].receiver() == Global.current_application_address(),
                Gtxn[1].close_remainder_to() == Global.zero_address(),
                App.optedIn(Int(1), Int(0)),
                is_empty (Tan.sender()),
                is_empty (Tan.accounts[1]),
                Txn.application_args.length() == Int(3),
            ),
        ),

        App.localPut (Txn.sender(), local_lab, Txn.accounts[1]),
        App.localPut (Txn.sender), local_wager, Gtxn[1].amount(),
        App.localPut (Txn.sender(), local_garden_id, Txn.application_args[1]),
        App.localPut (Txn.accounts[1], local_garden_id, Txn.application_args[1]),
        App.localPut (Txn.sender(), local_veggie_type, Btoi(Txn.application_args[2])),
        App.localPut (Txn.accounts[1], local_veggie_type, Btoi(Txn.application_args[2])),
        Approve(),
    )

@Subroutine (TealType.none) 
def accept_quality_check(): 
    return Seq(
        program.check_self(
            group_size=Int(1),
            group_index=Int(0),
        ),
        program.check_rekey_zero(1),
        Assert(
            And(
                App.optedIn(Txn.accounts[1], Global.current_application_id()),  
                App.localGet(Txn.accounts[1], local_lab) == Txn.sender(),
                Btoi(Txn.application_args[2]) == App.localGet(Txn.accounts[1],local_wager),
                Txn.application_args.length() == Int(3),
            ),
        ),
        App.localPut (Txn.sender(), local_lab, Txn.accounts[1]), 
        App.localPut (Txn.sender(), local_veggie_type, App.localGet(Txn.accounts[1], local_veggie_type)),
        App.localPut (Txn.sender(), local_wager, Btoi(Txn.application_args[2])),
        App.localPut (Txn.sender(), local_veggie_quality, Txn.application_args[1]),
        Approve(),
    )

@Subroutine (TealType.none) 
def resolve_quality_check(): 
    return Seq(
        program.check_self(
            group_size=Int(1),
            group_index=Int(0)
        ),
        program.check_rekey_zero(1),
        Assert(
            And(
                App.localGet(Txn.sender(), local_lab) == Txn.accounts[1],
                App.localGet(Txn.accounts[1],local_lab) == Txn.sender(),
                App.localGet(Txn.sender(), local_wager) == App.localGet(Txn.accounts[1], local_wager),
                App.localGet(Txn.accounts[1], local_veggie_quality) != Bytes(""),
                Txn.application_args.length() == Int(2),
            ),
        ),
        Seq(
            Assert (Txn.fee() >= Global.min_txn_fee() * Int(2)), send_payment (Int(1), App.localGet(Txn.sender(), local_wager)),
            App.localPut(Txn.sender(), local_veggie_quality, Txn.application_args[1])
        ),
        reset(Txn.sender()),
        reset(Txn.accounts[1]),
        Approve(),
    )

@Subroutine (TealType.none)
def send_payment (account_index: Expr, amount: Expr):
    return Seq(
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields({
            TxnField.type_enum: TxnType.Payment,
            TxnField.receiver: Txn.accounts[account_index],
            TxnField.amount: amount,
            TxnField.fee: Int(0)
}),
InnerTxnBuilder.Submit(),
)

def clear():
    return Approve()