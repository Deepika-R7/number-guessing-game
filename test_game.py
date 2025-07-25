import pytest
from game import NumberGuessingGame
from unittest.mock import patch
import random

@pytest.fixture
def game():
    return NumberGuessingGame()

def test_initial_high_scores(game):
    assert game.high_scores['easy'] == float('inf')
    assert game.high_scores['medium'] == float('inf')
    assert game.high_scores['hard'] == float('inf')

def test_get_difficulty_valid_input(game):
    with patch('builtins.input', return_value='2'):
        name, attempts = game.get_difficulty()
        assert name == 'medium'
        assert attempts == 5

def test_get_difficulty_invalid_then_valid_input(game):
    with patch('builtins.input', side_effect=['4', 'abc', '3']):
        name, attempts = game.get_difficulty()
        assert name == 'hard'
        assert attempts == 3

def test_get_hint(game):
    assert "very far" in game.get_hint(50, 10)
    assert "getting warmer" in game.get_hint(50, 30)
    assert "getting close" in game.get_hint(50, 45)
    assert "very close" in game.get_hint(50, 49)

def test_play_round_win(game, monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 42)
    inputs = ['2', '50', '30', '40', '42']  # difficulty medium, then guesses
    with patch('builtins.input', side_effect=inputs):
        with patch('time.time', side_effect=[0, 1, 2, 3, 4]):  # mock timer
            game.run()
    assert game.high_scores['medium'] == 4

def test_play_round_lose(game, monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 42)
    inputs = ['3', '10', '20', '30', 'n']  # difficulty hard, then guesses, then no replay
    with patch('builtins.input', side_effect=inputs):
        game.run()
    assert game.high_scores['hard'] == float('inf')  # no win, so high score remains
