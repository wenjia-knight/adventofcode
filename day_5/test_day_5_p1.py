from day_5_p1 import parse_instruction, move_crate, move_crates
import unittest 
import pytest 

def test_parse_instruction():
    # Given
    instruction = 'move 1 from 2 to 1'
    expected_instruction = (1,2,1)
    # When
    actual_instruction = parse_instruction(instruction=instruction) 
    # Then
    assert expected_instruction==actual_instruction


def test_move_crate():
    crate_stacks = [                                                 
        ['Z','N'],['M','C','D'],['P']       #given there are crates #
    ]
    instruction = 'move 1 from 2 to 1'
    expected_crates = [['Z','N','D'],['M','C'],['P']]

    actual_crates = move_crate(crate_stacks=crate_stacks,instruction=instruction)     #when#

    assert expected_crates==actual_crates #then#


def test_move_crates():
    crate_stacks = [                                                 
        ['Z','N'],['M','C','D'],['P']       #given there are crates #
    ]
    instructions = ['move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1','move 1 from 1 to 2']
    expected_crates = [['C'],['M'],['P','D','N','Z']]

    actual_crates = move_crates(crate_stacks=crate_stacks,instructions=instructions)     #when#

    assert expected_crates==actual_crates #then#