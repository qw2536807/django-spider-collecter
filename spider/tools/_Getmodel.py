def model_getattr(model_obj, field, attr):
    '''
    将一个model对象转换成字典

    '''

    for i in model_obj._meta.fields:
        name = i.attname                 # 获取字段名
        if name == field:
            return getattr(i, attr)
    return False
