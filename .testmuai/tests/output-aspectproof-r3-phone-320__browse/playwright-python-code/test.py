import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="94eb5f31-da3a-4ffe-bc69-359c52d8bdf0",
    name="Verify Shop Page Functionality on Small Android Screen",
    tc_id="TC-23",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"header_navigation_links_visible": "false", "shop_product_count": "4", "listed_product_prices": "true", "listed_product_add_to_cart_buttons": "true", "issues_seen_this_session": "true", "layout_report": "AspectProof layout\nPhone 320\u00d7568 (small Android) \u00b7 portrait\nProbe: active (138 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-320&run=r3-phone-320__browse&start=%2F', instruction_id='b1f8dbdb-9be3-475b-9321-114258933060'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-320&run=r3-phone-320__browse&start=%2F")
    
    async with testmu.step("whether the site's header navigation links are visible in the header", instruction_id='f29a9f7c-f52a-446a-93a4-b18f474a33a4'):
        set_var('header_navigation_links_visible', await testmu.vision_query(page, "whether the site's header navigation links are visible in the header", ""))
    if await testmu.evaluate_branch(sub_checks=[{'description': "the site's header navigation links are not visible", 'store_key': 'header_navigation_links_visible', 'expected_value': 'false', 'stored_value': '{{header_navigation_links_visible}}', 'extracted_value': '{{header_navigation_links_visible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
        
        async with testmu.step('Clicking the Menu button in the top-right header', instruction_id='6f436bc4-9001-4d20-95f3-937399a43ca1'):
            _loc_2 = frame_0.locator("internal:role=button[name=\"Menu\"i]")
            
            await _loc_2.click()
            # Reset to main page context
    frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Shop in the header navigation menu', instruction_id='1808ef26-e9e1-41d7-b4ff-831c729fcf64'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Shop\"s]")
        
        await _loc_4.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Shop page heading to be visible', instruction_id='57a3f1ae-324b-4747-b742-e6522a52148d'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the heading 'Shop' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Counting products in the Shop list'):
        set_var('shop_product_count', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).querySelectorAll(':scope > article').length);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='the number of product articles in the Shop product list', expected_value='3', needs_unit_conversion=False, operator='gte', transforms=[], condition='At least 3 products are listed.'))
    
    async with testmu.step('Checking for prices on listed products'):
        set_var('listed_product_prices', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(9).querySelectorAll(':scope > article')).filter(article => /(?:\\$|€|£)\\s*\\d+(?:\\.\\d{2})?/.test(article.innerText)).length >= 3);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether prices for at least 3 listed products are present in the Shop product list', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Each of at least 3 listed products has a price.'))
    
    async with testmu.step('Checking for Add to cart buttons on listed products'):
        set_var('listed_product_add_to_cart_buttons', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(9).querySelectorAll(':scope > article')).filter(article => Array.from(article.querySelectorAll('button')).some(button => button.textContent.trim() === 'Add to cart')).length >= 3);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Trail Runner Shoes $129.00 Add to cart Daypack 22L $89.00 Add to cart Storm"i'], query='whether Add to cart buttons for at least 3 listed products are present in the Shop product list', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="Each of at least 3 listed products has an 'Add to cart' button."))
    
    async with testmu.step('Assertion check', instruction_id='e627c68d-3a44-433a-9c6e-98d15374ad39'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'At least 3 products are listed.', 'passed': True, 'operator': 'gte', 'transforms': [], 'json_path': None, 'expected': '3', 'extracted_value': '{{shop_product_count}}', 'store_key': 'shop_product_count', 'variable_refs': {'{{shop_product_count}}': '4'}}, {'description': 'Each of at least 3 listed products has a price.', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_product_prices}}', 'store_key': 'listed_product_prices', 'variable_refs': {'{{listed_product_prices}}': 'true'}}, {'description': "Each of at least 3 listed products has an 'Add to cart' button.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{listed_product_add_to_cart_buttons}}', 'store_key': 'listed_product_add_to_cart_buttons', 'variable_refs': {'{{listed_product_add_to_cart_buttons}}': 'true'}}], 'sub_checks': [{'description': 'At least 3 products are listed.', 'store_key': 'shop_product_count', 'expected_value': '3', 'extracted_value': '{{shop_product_count}}', 'operator': 'gte', 'transforms': []}, {'description': 'Each of at least 3 listed products has a price.', 'store_key': 'listed_product_prices', 'expected_value': 'true', 'extracted_value': '{{listed_product_prices}}', 'operator': 'equals', 'transforms': []}, {'description': "Each of at least 3 listed products has an 'Add to cart' button.", 'store_key': 'listed_product_add_to_cart_buttons', 'expected_value': 'true', 'extracted_value': '{{listed_product_add_to_cart_buttons}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "At least 3 products are listed, each with a price and an 'Add to cart' button."})
    
    async with testmu.step('Reading the full AspectProof layout panel text without interacting', instruction_id='3c6b8405-84f6-4f4e-912d-30491eea05aa'):
        await page.wait_for_timeout(100)
    
    async with testmu.step('Checking whether the session issue count is present'):
        set_var('issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {28: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(28).innerText.trim() === 'Issues seen this session: 0');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query='whether the text "Issues seen this session: 0" is present in the AspectProof layout panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {25: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(25).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full "AspectProof layout" panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='d519d73c-5998-4d2a-a5b8-1a0826bfdcd2'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{issues_seen_this_session}}', 'store_key': 'issues_seen_this_session', 'variable_refs': {'{{issues_seen_this_session}}': 'true'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'issues_seen_this_session', 'expected_value': 'true', 'extracted_value': '{{issues_seen_this_session}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)