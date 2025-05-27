import unittest
from unittest.mock import MagicMock, patch
from midi_keyboard import Keyboard, Event, EventType

class TestKeyboard(unittest.TestCase):

    def setUp(self):
        self.queue_mock = MagicMock()
        self.keyboard = Keyboard(self.queue_mock)

    @patch('digitalio.DigitalInOut')
    def test_initialization(self, mock_digital_in_out):
        # Проверяем, что все кнопки инициализированы правильно
        self.assertEqual(len(self.keyboard.buttons), len(gps))
        self.assertEqual(len(self.keyboard.pressed), len(gps))
        self.assertEqual(len(self.keyboard.layout), len(gps))

    def test_read_buttons_no_change(self):
        # Симулируем ситуацию, когда состояние кнопок не изменилось
        self.keyboard.read_buttons()
        self.queue_mock.append.assert_not_called()

    def test_read_buttons_note_on(self):
        # Симулируем нажатие кнопки
        with patch.object(self.keyboard.buttons[0], 'value', new_callable=MagicMock, return_value=False):
            self.keyboard.read_buttons()
            self.queue_mock.append.assert_called_once_with(
                Event(type=EventType.NOTE_ON, value=self.keyboard.layout[0])
            )

    def test_read_buttons_note_off(self):
        # Симулируем отпускание кнопки
        self.keyboard.pressed[0] = True  # Предварительно нажимаем кнопку
        with patch.object(self.keyboard.buttons[0], 'value', new_callable=MagicMock, return_value=True):
            self.keyboard.read_buttons()
            self.queue_mock.append.assert_called_once_with(
                Event(type=EventType.NOTE_OFF, value=self.keyboard.layout[0])
            )

if __name__ == '__main__':
    unittest.main()
