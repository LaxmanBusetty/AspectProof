import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="7d2010a7-2962-4715-a953-204d07efd47a",
    name="Verify Shop Page Product Listings and Layout Status",
    tc_id="TC-5",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"shop_product_count_check": "4", "listed_products_price_present": "true", "listed_products_add_to_cart_button_present": "true", "layout_issues_seen_session_check": "0", "layout_report": "AspectProof layout\nDesktop 1920\u00d71080 (full window)\nProbe: active (66 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=desktop-1920&run=r3-desktop-1920__browse&start=%2F', instruction_id='01871382-f56c-4685-9e88-7397d17ed7a7'):
        await page.goto("http://localhost:4400/__ap/frame?profile=desktop-1920&run=r3-desktop-1920__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Shop in the header navigation', instruction_id='9192f394-014c-4a3a-b071-bdaab010a193'):
        _loc_2 = frame_0.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_2.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page heading to be visible', instruction_id='1b7a24b8-5bb7-409f-9410-b799b4ea0760'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the heading 'Shop' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting the listed shop products'):
        set_var('shop_product_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(12).querySelectorAll(':scope > article').length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='the number of product articles in the shop product list', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking whether every listed product has a price'):
        set_var('listed_products_price_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(12).querySelectorAll(':scope > article')).every(article => /(?:^|\\s)[$€£]\\s?\\d+(?:\\.\\d{2})?(?:\\s|$)/.test(article.innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether a price for each listed product is present in the shop product list', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each listed product has a price.'))
    
    async with testmu.step('Checking whether every listed product has an Add to cart button'):
        set_var('listed_products_add_to_cart_button_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(12).querySelectorAll(':scope > article')).every(article => Array.from(article.querySelectorAll('button')).some(button => button.innerText.trim() === 'Add to cart')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether an Add to cart button for each listed product is present in the shop product list', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Reading the session issue count from the layout panel'):
        set_var('layout_issues_seen_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText.match(/Issues seen this session:\\s*(\\d+)/)?.[1] ?? null);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the Issues seen this session count in the AspectProof layout panel', expected_value='0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Reading the full AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='9d22ff46-75e3-4ec4-bf85-aa44b56552e5'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{shop_product_count_check}}', 'store_key': 'shop_product_count_check', 'variable_refs': {'{{shop_product_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_products_price_present}}', 'store_key': 'listed_products_price_present', 'variable_refs': {'{{listed_products_price_present}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_products_add_to_cart_button_present}}', 'store_key': 'listed_products_add_to_cart_button_present', 'variable_refs': {'{{listed_products_add_to_cart_button_present}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'shop_product_count_check', 'expected_value': '3', 'extracted_value': '{{shop_product_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'listed_products_price_present', 'expected_value': 'true', 'extracted_value': '{{listed_products_price_present}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'listed_products_add_to_cart_button_present', 'expected_value': 'true', 'extracted_value': '{{listed_products_add_to_cart_button_present}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Assertion check', instruction_id='1d6eb77c-c9f1-4862-a05e-eea29e49c1fe'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '0', 'extracted_value': '{{layout_issues_seen_session_check}}', 'store_key': 'layout_issues_seen_session_check', 'variable_refs': {'{{layout_issues_seen_session_check}}': '0'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'layout_issues_seen_session_check', 'expected_value': '0', 'extracted_value': '{{layout_issues_seen_session_check}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)