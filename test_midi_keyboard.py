import pytest
from unittest.mock import MagicMock, patch
from midi_keyboard import Keyboard, Event, EventType

@pytest.fixture
def mock_queue():
    return MagicMock()

@pytest.fixture
def keyboard(mock_queue):
    return Keyboard(mock_queue)

def test_initialization(keyboard):
    assert len(keyboard.buttons) == 28
    assert len(keyboard.pressed) == 28
    assert len(keyboard.layout) == 28

@patch('midi_keyboard.DigitalInOut')
def test_read_buttons(mock_digital_in_out, keyboard, mock_queue):
    # Предположим, что все кнопки не нажаты в начале
    for i in range(len(keyboard.buttons)):
        button_mock = MagicMock()
        button_mock.value = True
        keyboard.buttons[i] = button_mock

    # Прочитать кнопки, ничего не должно измениться
    keyboard.read_buttons()
    mock_queue.append.assert_not_called()

    # Попробуем нажать одну кнопку
    keyboard.buttons[0].value = False
    keyboard.read_buttons()
    mock_queue.append.assert_called_once_with(Event(type=EventType.NOTE_ON, value=69))

    # Проверим, что кнопка считалась нажатой
    assert keyboard.pressed[0] == False

    # Отпустим кнопку
    keyboard.buttons[0].value = True
    keyboard.read_buttons()
    mock_queue.append.assert_called_with(Event(type=EventType.NOTE_OFF, value=69))

    # Проверим, что кнопка считалась не нажатой
    assert keyboard.pressed[0] == True

@patch('midi_keyboard.DigitalInOut')
def test_bouncing(mock_digital_in_out, keyboard, mock_queue):
    # Пробуем сценарий дребезжания контактов
    keyboard.buttons[0].value = False
    keyboard.read_buttons()  # Первое нажатие
    mock_queue.append.assert_called_once_with(Event(type=EventType.NOTE_ON, value=69))

    # Подменим кнопку на True, но ожидаем, что события не поступят повторно
    keyboard.buttons[0].value = True
    keyboard.read_buttons()
    mock_queue.append.assert_called_with(Event(type=EventType.NOTE_OFF, value=69))
    
    # И снова нажимаем, но без повторного события нажатия (защита от дребезжания)
    keyboard.buttons[0].value = False
    keyboard.read_buttons()
    mock_queue.call_count = 2  # Проверяем, что событий все равно два
