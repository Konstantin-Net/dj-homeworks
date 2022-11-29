import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


# проверка получения одного курса
@pytest.mark.django_db
def test_one_course(client, course_factory):
    one_course = course_factory()
    response = client.get(f'/api/v1/courses/?id={one_course.id}')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['name'] == one_course.name


# проверка получения списка курсов
@pytest.mark.django_db
def test_list_course(client, course_factory):
    list_course = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(list_course)


# проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_filter_id_course(client, course_factory):
    list_course = course_factory(_quantity=5)
    id_list = list_course[3].id
    response = client.get(f'/api/v1/courses/?id={id_list}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == id_list


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_filter_name_course(client, course_factory):
    list_course = course_factory(_quantity=5)
    name = list_course[3].name
    response = client.get(f'/api/v1/courses/?name={name}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == name


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'math'})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


# тест успешного обновления курса
@pytest.mark.django_db
def test_patch_course(client, course_factory):
    list_course = course_factory(_quantity=5)
    name_course = 'math'
    id_list = list_course[3].id
    response = client.patch(f'/api/v1/courses/{id_list}/', data={'name': name_course})
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == name_course


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    list_course = course_factory(_quantity=5)
    id_list = list_course[3].id
    response = client.delete(f'/api/v1/courses/{id_list}/')
    assert response.status_code == 204
    count = Course.objects.count()
    assert count == len(list_course) - 1
