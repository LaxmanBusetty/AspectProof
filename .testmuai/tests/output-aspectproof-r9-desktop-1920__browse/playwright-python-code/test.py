import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="585ab98a-e51c-43e4-898f-b52c170875b9",
    name="Verify Shop Page Product Listings and Layout Status",
    tc_id="TC-75",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"product_count_check": "4", "product_prices_present": "true", "add_to_cart_buttons_present": "true", "issues_seen_this_session_check": "AspectProof layout\nDesktop 1920\u00d71080 (full window)\nProbe: active (94 scans)\nIssues now: 0\nIssues seen this session: 0", "layout_report": "AspectProof layout\nDesktop 1920\u00d71080 (full window)\nProbe: active (94 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=desktop-1920&run=r9-desktop-1920__browse&start=%2F', instruction_id='dce36f8c-e7e6-44cf-9cd3-1f082398a655'):
        await page.goto("http://localhost:4400/__ap/frame?profile=desktop-1920&run=r9-desktop-1920__browse&start=%2F")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Shop link in the header navigation', instruction_id='514c4f1d-e619-4133-8129-641ba2f25b47'):
        _loc_2 = frame_0.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_2.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page to load', instruction_id='aaee68dd-aa98-4576-9f3d-1ac8d1e618c1'):
            await page.wait_for_timeout(1000)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the heading 'Shop' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting products in the shop list'):
        set_var('product_count_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(12).querySelectorAll(':scope > article').length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='the number of product articles in the shop product list', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking whether listed products have prices'):
        set_var('product_prices_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(12).querySelectorAll(':scope > article')).every(article => /(?:\\$|€|£)\\s*\\d+(?:\\.\\d{2})?/.test(article.innerText)));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether a price for each listed product is present in the shop product list', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each listed product has a price.'))
    
    async with testmu.step('Checking whether listed products have Add to cart buttons'):
        set_var('add_to_cart_buttons_present', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(12).querySelectorAll(':scope > article')).every(article => Array.from(article.querySelectorAll('button')).some(button => button.innerText.trim() === 'Add to cart')));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query="whether an 'Add to cart' button for each listed product is present in the shop product list", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each listed product has an 'Add to cart' button."))
    
    async with testmu.step('Assertion check', instruction_id='81bfde66-958e-4817-9efb-9fe6d121cbaf'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{product_count_check}}', 'store_key': 'product_count_check', 'variable_refs': {'{{product_count_check}}': '4'}}, {'description': 'Each listed product has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{product_prices_present}}', 'store_key': 'product_prices_present', 'variable_refs': {'{{product_prices_present}}': 'true'}}, {'description': "Each listed product has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{add_to_cart_buttons_present}}', 'store_key': 'add_to_cart_buttons_present', 'variable_refs': {'{{add_to_cart_buttons_present}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'product_count_check', 'expected_value': '3', 'extracted_value': '{{product_count_check}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each listed product has a price.', 'store_key': 'product_prices_present', 'expected_value': 'true', 'extracted_value': '{{product_prices_present}}', 'operator': 'equals', 'transforms': []}, {'description': "Each listed product has an 'Add to cart' button.", 'store_key': 'add_to_cart_buttons_present', 'expected_value': 'true', 'extracted_value': '{{add_to_cart_buttons_present}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Reading the issue count from the AspectProof layout panel'):
        set_var('issues_seen_this_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the issue count text in the AspectProof layout panel', expected_value='Issues seen this session: 0', needs_unit_conversion=False, operator='contains', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='837a18d2-cc07-4124-ac44-81df3bb30690'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'contains', 'transforms': [], 'json_path': None, 'expected': 'Issues seen this session: 0', 'extracted_value': '{{issues_seen_this_session_check}}', 'store_key': 'issues_seen_this_session_check', 'variable_refs': {'{{issues_seen_this_session_check}}': 'AspectProof layout\nDesktop 1920×1080 (full window)\nProbe: active (94 scans)\nIssues now: 0\nIssues seen this session: 0'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'issues_seen_this_session_check', 'expected_value': 'Issues seen this session: 0', 'extracted_value': '{{issues_seen_this_session_check}}', 'operator': 'contains', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)