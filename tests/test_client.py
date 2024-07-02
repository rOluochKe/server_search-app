import pytest
from unittest.mock import patch
from ..client import main


def test_successful_connection(capsys):
    """Test successful connection to the server."""
    with patch('builtins.input', side_effect=["8080", "exit"]):
        main()
    captured = capsys.readouterr()
    assert "Exiting the client..." in captured.out


def test_query_response(capsys):
    """Test sending a query and receiving a response from the server."""
    with patch('builtins.input', side_effect=["8080", "test_query", "exit"]):
        with patch('socket.socket') as mock_socket:
            mock_socket_instance = mock_socket.return_value.__enter__.return_value
            mock_socket_instance.recv.return_value = b"STRING EXISTS"
            main()
    captured = capsys.readouterr()
    assert "STRING EXISTS" in captured.out


def test_exit_signal(capsys):
    """Test exiting the client."""
    with patch('builtins.input', side_effect=["8080", "exit"]):
        main()
    captured = capsys.readouterr()
    assert "Exiting the client..." in captured.out


def test_keyboard_interrupt(capsys):
    """Test handling KeyboardInterrupt."""
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = KeyboardInterrupt
        with pytest.raises(SystemExit):
            main()
    captured = capsys.readouterr()
    assert "Exiting the client..." in captured.out


def test_exception_handling(capsys):
    """Test handling exceptions."""
    with patch('builtins.input', side_effect=["8080", "test_query", "exit"]):
        with patch('socket.socket') as mock_socket:
            mock_socket_instance = mock_socket.return_value.__enter__.return_value
            mock_socket_instance.recv.side_effect = Exception(
                "Connection error")
            main()
    captured = capsys.readouterr()
    assert "Error: Connection error" in captured.out
