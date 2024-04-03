import pytest
from unittest.mock import patch
import pygame
import project


@pytest.fixture
def target():
    return project.Target(100, 100)


def test_target_creation(target):
    assert target.x == 100
    assert target.y == 100
    assert target.size == 0
    assert target.grow is True


def test_target_update(target):
    target.update()
    assert target.size == project.Target.GROWTH_RATE


def test_target_draw(target):
    pygame.init()
    win = pygame.display.set_mode((project.WIDTH, project.HEIGHT))
    target.draw(win)
    assert len(pygame.draw.circle.mock_calls) == 4  # Assuming draw.circle is properly patched


def test_target_collide(target):
    assert target.collide(105, 105) is True
    assert target.collide(200, 200) is False


def test_format_time():
    assert project.format_time(60) == "01:00.0"


def test_get_middle():
    assert project.get_middle(pygame.Surface((100, 50))) == project.WIDTH / 2 - 50


@patch('pygame.time.set_timer')
def test_main(set_timer_mock):
    with patch('project.pygame.quit'):
        with patch('project.pygame.display.update'):
            with patch('project.pygame.display.set_mode'):
                with patch('project.pygame.quit'):
                    project.main()
    set_timer_mock.assert_called_once_with(project.TARGET_EVENT, project.TARGET_INCREMENT)


if __name__ == "__main__":
    pytest.main()
