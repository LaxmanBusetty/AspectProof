import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="f3e77e0e-8680-483b-ba2d-a4d08142decf",
    name="Verify Shop Page and Layout Panel on Mobile",
    tc_id="TC-87",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"shop_product_count_check": "4", "product_prices_present": "true", "add_to_cart_buttons_present": "true", "aspectproof_issues_seen_check": "true", "layout_report": "AspectProof layout\nPhone 390\u00d7844 (iPhone 14) \u00b7 portrait\nProbe: active (72 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-390&run=r9-phone-390__browse&start=%2F', instruction_id='cfd4634f-4a07-4a64-a367-0807a628df1f'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-390&run=r9-phone-390__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Menu button in the top right', instruction_id='1eaec71d-be99-45a3-adda-a9c32b8ad9d7'):
        _loc_2 = frame_0.locator("internal:role=button[name=\"Menu\"i]")
        
        await _loc_2.click()
        # Reset to main page context
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Shop link in the header menu', instruction_id='d74df220-0946-4c99-83b0-daca34345142'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_4.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page to finish loading', instruction_id='6e9620c3-d974-4c77-9fe1-ae23abf336ea'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, 'the heading "Shop" is visible'):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting listed products in the shop'):
        set_var('shop_product_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).querySelectorAll(':scope > article').length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='the number of listed product cards in the Shop product grid', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking whether every listed product has a price'):
        set_var('product_prices_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const products = Array.from(el(9).querySelectorAll(':scope > article')); return products.length > 0 && products.every(product => /(?:\\$|€|£)\\s*\\d+(?:\\.\\d{2})?/.test(product.innerText)); })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether a price for each listed product is present in the Shop product grid', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each listed product has a price.'))
    
    async with testmu.step('Checking whether every listed product has an Add to cart button'):
        set_var('add_to_cart_buttons_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((() => { const products = Array.from(el(9).querySelectorAll(':scope > article')); return products.length > 0 && products.every(product => Array.from(product.querySelectorAll('button')).some(button => button.innerText.trim() === 'Add to cart')); })());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether an Add to cart button for each listed product is present in the Shop product grid', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Checking whether the AspectProof layout panel shows zero session issues'):
        set_var('aspectproof_issues_seen_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {25: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(25).innerText.includes('Issues seen this session: 0'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether Issues seen this session: 0 is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Reading the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {25: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(25).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full "AspectProof layout" panel text is saved as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='4e8b827b-39df-439c-bc85-667e342ad57f'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{shop_product_count_check}}', 'store_key': 'shop_product_count_check', 'variable_refs': {'{{shop_product_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{product_prices_present}}', 'store_key': 'product_prices_present', 'variable_refs': {'{{product_prices_present}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{add_to_cart_buttons_present}}', 'store_key': 'add_to_cart_buttons_present', 'variable_refs': {'{{add_to_cart_buttons_present}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'shop_product_count_check', 'expected_value': '3', 'extracted_value': '{{shop_product_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'product_prices_present', 'expected_value': 'true', 'extracted_value': '{{product_prices_present}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'add_to_cart_buttons_present', 'expected_value': 'true', 'extracted_value': '{{add_to_cart_buttons_present}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Assertion check', instruction_id='e788afaf-5d8c-4841-a2d0-27ef8b4b511d'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{aspectproof_issues_seen_check}}', 'store_key': 'aspectproof_issues_seen_check', 'variable_refs': {'{{aspectproof_issues_seen_check}}': 'true'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'aspectproof_issues_seen_check', 'expected_value': 'true', 'extracted_value': '{{aspectproof_issues_seen_check}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)