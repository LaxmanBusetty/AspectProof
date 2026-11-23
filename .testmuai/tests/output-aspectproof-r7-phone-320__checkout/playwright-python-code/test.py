import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="ed8a5dce-e715-4519-a96f-264243338d7e",
    name="Web || laxmanbusetty || TC-69",
    tc_id="TC-69",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"header_navigation_links_visible": "false", "order_confirmed_message_visible": "true", "aspectproof_layout_issues_seen_session_check": "0", "layout_report": "AspectProof layout\nPhone 320\u00d7568 (small Android) \u00b7 portrait\nProbe: active (187 scans)\nIssues now: 0\nIssues seen this session: 0", "layout_report_2": "AspectProof layout\nPhone 320\u00d7568 (small Android) \u00b7 portrait\nProbe: active (187 scans)\nIssues now: 0\nIssues seen this session: 0", "task_completion_at_screen_size_check": "true", "aspectproof_layout_issues_present_check": "false"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=phone-320&run=r7-phone-320__checkout&start=%2F%23shop', instruction_id='e1a43d53-fcb1-4419-9e43-5a191a488e28'):
        await page.goto("http://localhost:4400/__ap/frame?profile=phone-320&run=r7-phone-320__checkout&start=%2F%23shop")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Add to cart for Trail Runner Shoes', instruction_id='1f4266e2-93c9-4ad9-ba43-fee049753558'):
        _loc_2 = frame_0.locator("internal:role=article >> internal:has-text=\"Trail Runner Shoes $129.00\"i >> internal:role=button")
        
        await _loc_2.click()
        # Reset to main page context
    
    async with testmu.step("whether the site's header navigation links are visible in the header", instruction_id='26636c15-ddb9-45e8-8a26-ee545f2da0aa'):
        set_var('header_navigation_links_visible', await testmu.vision_query(page, "whether the site's header navigation links are visible in the header", ""))
    if await testmu.evaluate_branch(sub_checks=[{'description': "the site's header navigation links are not visible", 'store_key': 'header_navigation_links_visible', 'expected_value': 'false', 'stored_value': '{{header_navigation_links_visible}}', 'extracted_value': '{{header_navigation_links_visible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
        
        async with testmu.step('Clicking the Menu button in the top-right header', instruction_id='69810048-85fa-489c-8293-260a220d6306'):
            _loc_4 = frame_2.locator("internal:role=button[name=\"Menu\"i]")
            
            await _loc_4.click()
            # Reset to main page context
    frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Cart (1) in the header navigation', instruction_id='c6c79474-623c-4a36-919f-61b13ae369d0'):
        _loc_6 = frame_4.locator("internal:role=link[name=\"Cart (1)\"i]")
        
        await _loc_6.click()
        # Reset to main page context
        frame_6 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Typing 2 into cart quantity for Trail Runner Shoes', instruction_id='c1a880c9-a65a-4129-b360-54ef88f2f8a0'):
        element_0 = frame_6.locator("internal:role=spinbutton[name=\"Quantity for Trail Runner\"i]")
        
        await testmu.fill(element_0, "2")
        # Reset to main page context
        frame_7 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Place order', instruction_id='0c379baf-dc80-40f7-a64f-433b184f6d56'):
        _loc_9 = frame_7.locator("internal:role=button[name=\"Place order\"i]")
        
        await _loc_9.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the order confirmation message is present'):
        set_var('order_confirmed_message_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {9: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(9).innerText.includes('Order confirmed') && !!(el(9).offsetWidth || el(9).offsetHeight || el(9).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Order confirmed! 2 items, $"i'], query="whether an 'Order confirmed' message is present in the order status area", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="an 'Order confirmed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='918ed4ec-1479-410f-abdc-0ae6e681ac1d'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "an 'Order confirmed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{order_confirmed_message_visible}}', 'store_key': 'order_confirmed_message_visible', 'variable_refs': {'{{order_confirmed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "an 'Order confirmed' message appears", 'store_key': 'order_confirmed_message_visible', 'expected_value': 'true', 'extracted_value': '{{order_confirmed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "an 'Order confirmed' message appears"})
    
    async with testmu.step('Waiting for AspectProof layout panel to appear', instruction_id='bafb2ba3-75f4-4758-a288-23d991e68c2a'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Reading the session issue count from the AspectProof layout panel'):
        set_var('aspectproof_layout_issues_seen_session_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {17: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(17).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['#ap-seen'], query='the Issues seen this session value in the AspectProof layout panel', expected_value='0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Assertion check', instruction_id='bb4bf647-2312-400e-89e8-60227794213f'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '0', 'extracted_value': '{{aspectproof_layout_issues_seen_session_check}}', 'store_key': 'aspectproof_layout_issues_seen_session_check', 'variable_refs': {'{{aspectproof_layout_issues_seen_session_check}}': '0'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'aspectproof_layout_issues_seen_session_check', 'expected_value': '0', 'extracted_value': '{{aspectproof_layout_issues_seen_session_check}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(13).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report_2', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(13).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full "AspectProof layout" panel text is saved as {{layout_report}}', reprobe=True))
    
    async with testmu.step('whether an order confirmation indicating task completion is visible in the phone-sized storefront viewport', instruction_id='4868cfc1-62f3-4977-9654-c7c0c1d3d59d'):
        set_var('task_completion_at_screen_size_check', await testmu.vision_query(page, "whether an order confirmation indicating task completion is visible in the phone-sized storefront viewport", ""))
    
    async with testmu.step('Checking whether the AspectProof layout panel reports issues'):
        set_var('aspectproof_layout_issues_present_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {13: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(13).querySelectorAll('strong')).some(e => Number(e.textContent.trim()) > 0));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether the issue counts in the "AspectProof layout" panel are greater than zero', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the "AspectProof layout" panel shows any issues'))
    if await testmu.evaluate_branch(sub_checks=[{'description': 'the task cannot be completed at this screen size', 'store_key': 'task_completion_at_screen_size_check', 'expected_value': 'false', 'stored_value': '{{task_completion_at_screen_size_check}}', 'extracted_value': '{{task_completion_at_screen_size_check}}', 'operator': 'equals', 'transforms': []}, {'description': 'the "AspectProof layout" panel shows any issues', 'store_key': 'aspectproof_layout_issues_present_check', 'expected_value': 'true', 'stored_value': '{{aspectproof_layout_issues_present_check}}', 'extracted_value': '{{aspectproof_layout_issues_present_check}}', 'operator': 'equals', 'transforms': []}], composite_operator="or"):
        page = await testmu.execute_kane_cli('name the exact control or step that was blocked and why', page=page)


if __name__ == "__main__":
    testmu.run(test)