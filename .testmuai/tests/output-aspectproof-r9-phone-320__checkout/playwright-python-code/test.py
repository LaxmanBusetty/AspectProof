import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="612d36e6-4ecd-4d76-8fc6-a0518d82f7f9",
    name="Add and Order Trail Runner Shoes",
    tc_id="TC-94",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"header_navigation_links_visible": "false", "order_confirmed_message": "true", "issues_seen_this_session_check": "0", "layout_report": "AspectProof layout\nPhone 320\u00d7568 (small Android) \u00b7 portrait\nProbe: active (147 scans)\nIssues now: 0\nIssues seen this session: 0", "layout_report_2": "AspectProof layout\nPhone 320\u00d7568 (small Android) \u00b7 portrait\nProbe: active (147 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-320&run=r9-phone-320__checkout&start=%2F%23shop', instruction_id='8ebb54ce-2dce-4617-9763-16d6305e9352'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-320&run=r9-phone-320__checkout&start=%2F%23shop")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Add to cart for Trail Runner Shoes', instruction_id='3b125161-ef10-4743-908a-df452c692f0a'):
        _loc_2 = frame_0.locator("internal:role=article >> internal:has-text=\"Trail Runner Shoes $129.00\"i >> internal:role=button")
        
        await _loc_2.click()
        # Reset to main page context
    
    async with testmu.step("whether the site's header navigation links are visible in the header", instruction_id='682e8729-247e-4cae-92fd-b2e3f41d1aba'):
        set_var('header_navigation_links_visible', await testmu.vision_query(page, "whether the site's header navigation links are visible in the header", ""))
    if await testmu.evaluate_branch(sub_checks=[{'description': "the site's header navigation links are not visible", 'store_key': 'header_navigation_links_visible', 'expected_value': 'false', 'stored_value': '{{header_navigation_links_visible}}', 'extracted_value': '{{header_navigation_links_visible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
        
        async with testmu.step('Clicking Menu button', instruction_id='a5f25ed8-b213-4457-b1ed-5cd002f58a00'):
            _loc_4 = frame_2.locator("internal:role=button[name=\"Menu\"i]")
            
            await _loc_4.click()
            # Reset to main page context
    frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Cart (1) in the header navigation', instruction_id='6b985bd2-cfab-446f-ab7c-a536d4b83bb1'):
        _loc_6 = frame_4.locator("internal:role=link[name=\"Cart (1)\"i]")
        
        await _loc_6.click()
        # Reset to main page context
    
    async with testmu.step('Waiting for order placement to proceed', instruction_id='949d1427-9014-4636-a467-8aaee9bf0563'):
        await page.wait_for_timeout(1000)
        frame_6 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "2" into "Quantity for Trail Runner Shoes"', instruction_id='28395b6c-966a-45fd-bbce-52d5a9b078fd'):
        element_0 = frame_6.locator("internal:role=spinbutton[name=\"Quantity for Trail Runner\"i]")
        
        await testmu.fill(element_0, "2")
        # Reset to main page context
        frame_7 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Click "Place order"', instruction_id='c3674e65-83a1-42c8-803f-0199fd744931'):
        _loc_9 = frame_7.locator("internal:role=button[name=\"Place order\"i]")
        
        await _loc_9.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the order confirmation message is present'):
        set_var('order_confirmed_message', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).innerText.includes('Order confirmed'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Order confirmed! 2 items, $"i'], query="whether an 'Order confirmed' message is present in the order status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="an 'Order confirmed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='99efa2ee-3bd4-472c-9049-e8956c7c8ef6'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "an 'Order confirmed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{order_confirmed_message}}', 'store_key': 'order_confirmed_message', 'variable_refs': {'{{order_confirmed_message}}': 'true'}}], 'sub_checks': [{'description': "an 'Order confirmed' message appears", 'store_key': 'order_confirmed_message', 'expected_value': 'true', 'extracted_value': '{{order_confirmed_message}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "an 'Order confirmed' message appears"})
    
    async with testmu.step('Reading the session issue count from the AspectProof layout panel'):
        set_var('issues_seen_this_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {17: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(17).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['#ap-seen'], query='the Issues seen this session count in the AspectProof layout panel', expected_value='0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(13).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report_2', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(13).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}', reprobe=True))
    
    async with testmu.step('Assertion check', instruction_id='84fc1fa3-3c3b-4350-b612-c6fa40a09eb6'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '0', 'extracted_value': '{{issues_seen_this_session_check}}', 'store_key': 'issues_seen_this_session_check', 'variable_refs': {'{{issues_seen_this_session_check}}': '0'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'issues_seen_this_session_check', 'expected_value': '0', 'extracted_value': '{{issues_seen_this_session_check}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)