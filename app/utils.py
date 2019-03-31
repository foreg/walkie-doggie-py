def login_required(function_to_decorate):
    def check(*args, **kwargs):
        from flask_login import current_user
        from flask import redirect, url_for
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        return function_to_decorate(*args, **kwargs)
    return check

def fill_entity(entity, form, needed = [], aliases = {}):
    """Заполняет сущность данными из формы

    Arguments:
        entity {object} -- Сущность, которую нужно заполнить
        form {FlaskForm} -- Форма, источник данных
    
    Keyword Arguments:
        aliases {dict} -- Словарь типа {'name_in_entity':'name_in_form'} в случае если поля на форме и у сущности называются по разному
        needed {list} -- Лист нужных для заполнения полей. Если не указан - заполняются все поля
    
    Returns:
        [list,list] -- Лист полей с ошибками и лист успешно обновленных полей
    """

    errors = []
    successfully = []
    for field in form.data:
        if field in form.ignored_fields:
            continue
        field_name = aliases.get(field, field)
        if len(needed) > 0 and field_name not in needed:
            continue
        if getattr(entity, '{}'.format(field_name), False):
            setattr(entity, '{}'.format(field_name), form.data[field_name])
            successfully.append(field_name)
        else:
            errors.append(field_name)
    return errors, successfully

def fill_entities(entities, form, needed={}, aliases = {}):
    """Заполняет несколько сущностей данными из формы
    
    Arguments:
        entities {list} -- Лист сущностей
        form {FlaskForm} -- Форма, источник данных
    
    Keyword Arguments: 
        aliases {dict} -- Словарь типа {entity_name: {'name_in_entity':'name_in_form'}} в случае если поля на форме и у сущности называются по разному
        needed {dict} -- Словарь типа {entity_name: ['field_name']} для указание нужных для заполнения полей. Если не указан - заполняются все поля
    Returns:
        [list] -- Лист объектов типа {entity, errors, successfully}
    """

    results = []
    for entity in entities:
        errors, successfully = fill_entity(entity, form, needed = needed.get(entity,[]), aliases = aliases.get(entity,{}))
        result = {
            entity: entity, 
            errors: errors,
            successfully: successfully
        }
        results.append(result)
    return results