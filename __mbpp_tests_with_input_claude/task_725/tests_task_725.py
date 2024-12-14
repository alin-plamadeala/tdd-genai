from solution_task_725 import extract_quotation

def test_0():
    assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']

def test_1():
    assert extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']

def test_2():
    assert extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']

