import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="5e2979fe-e2bd-4296-84b7-eb9a285e3124",
    name="Add and Order Trail Runner Shoes",
    tc_id="TC-91",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"header_navigation_links_visible": "false", "order_confirmed_message_visible": "true", "issues_seen_this_session_zero": "true", "layout_report": "AspectProof layout\nPhone 375\u00d7812 (iPhone 11 Pro) \u00b7 portrait\nProbe: active (170 scans)\nIssues now: 0\nIssues seen this session: 0", "layout_report_2": "AspectProof layout\nPhone 375\u00d7812 (iPhone 11 Pro) \u00b7 portrait\nProbe: active (170 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-375&run=r9-phone-375__checkout&start=%2F%23shop', instruction_id='4f4b194c-ed80-4b5a-8653-f7d2224c5005'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-375&run=r9-phone-375__checkout&start=%2F%23shop")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Add to cart for Trail Runner Shoes', instruction_id='60dd67c1-24f1-47b1-b6de-b318d832fc82'):
        _loc_2 = frame_0.locator("internal:role=article >> internal:has-text=\"Trail Runner Shoes $129.00\"i >> internal:role=button")
        
        await _loc_2.click()
        # Reset to main page context
    
    async with testmu.step("whether the site's header navigation links are visible in the header", instruction_id='b3548e9c-8281-428f-a27b-7d3ff523a0f5'):
        set_var('header_navigation_links_visible', await testmu.vision_query(page, "whether the site's header navigation links are visible in the header", ""))
    if await testmu.evaluate_branch(sub_checks=[{'description': "the site's header navigation links are not visible", 'store_key': 'header_navigation_links_visible', 'expected_value': 'false', 'stored_value': '{{header_navigation_links_visible}}', 'extracted_value': '{{header_navigation_links_visible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
        
        async with testmu.step('Clicking the Menu button in the top-right header', instruction_id='b6186476-ce68-4386-9218-4643e0bfca7d'):
            _loc_4 = frame_2.locator("internal:role=button[name=\"Menu\"i]")
            
            await _loc_4.click()
            # Reset to main page context
    frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Cart link in the header navigation', instruction_id='1ca2c846-f431-45bc-b5e4-82825dd18c19'):
        _loc_6 = frame_4.locator("internal:role=link[name=\"Cart (1)\"i]")
        
        await _loc_6.click()
        # Reset to main page context
    
    async with testmu.step('Waiting for the order to be placed', instruction_id='579fd9dd-c7a1-48a5-aedb-0cf87beb1dbc'):
        await page.wait_for_timeout(1000)
        frame_6 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "2" into "Quantity for Trail Runner Shoes"', instruction_id='7454eb13-88c0-41a1-9350-fc1299fcbf77'):
        element_0 = frame_6.locator("internal:role=spinbutton[name=\"Quantity for Trail Runner\"i]")
        
        await testmu.fill(element_0, "2")
        # Reset to main page context
        frame_7 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Click "Place order"', instruction_id='32b4cef5-8672-4322-bb11-29563b0204b0'):
        _loc_9 = frame_7.locator("internal:role=button[name=\"Place order\"i]")
        
        await _loc_9.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the order confirmation message is present'):
        set_var('order_confirmed_message_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).innerText.includes('Order confirmed'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Order confirmed! 2 items, $"i'], query="whether an 'Order confirmed' message is present in the order status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="an 'Order confirmed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='776e248c-7ed3-44ae-b9e2-205c7dd90ebc'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "an 'Order confirmed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{order_confirmed_message_visible}}', 'store_key': 'order_confirmed_message_visible', 'variable_refs': {'{{order_confirmed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "an 'Order confirmed' message appears", 'store_key': 'order_confirmed_message_visible', 'expected_value': 'true', 'extracted_value': '{{order_confirmed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "an 'Order confirmed' message appears"})
    
    async with testmu.step('Checking whether the session issue count is present in the layout panel'):
        set_var('issues_seen_this_session_zero', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(13).innerText.includes('Issues seen this session: 0'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether the AspectProof layout panel contains the text "Issues seen this session: 0"', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(13).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report_2', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(13).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}', reprobe=True))
    
    async with testmu.step('Assertion check', instruction_id='0ffc7267-824e-4930-97d2-82901897eda4'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{issues_seen_this_session_zero}}', 'store_key': 'issues_seen_this_session_zero', 'variable_refs': {'{{issues_seen_this_session_zero}}': 'true'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'issues_seen_this_session_zero', 'expected_value': 'true', 'extracted_value': '{{issues_seen_this_session_zero}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'it shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)