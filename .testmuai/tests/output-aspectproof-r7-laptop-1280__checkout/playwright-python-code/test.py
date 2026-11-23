import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="c1cc244f-d61f-4234-a089-f23d236ae121",
    name="Add and Order Trail Runner Shoes",
    tc_id="TC-54",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"header_navigation_links_visible": "true", "order_confirmed_message_visible": "true", "aspectproof_layout_issues_seen_session": "0", "layout_report": "AspectProof layout\nLaptop 1280\u00d7800 (full window)\nProbe: active (126 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=laptop-1280&run=r7-laptop-1280__checkout&start=%2F%23shop', instruction_id='8cd36804-85f2-4dba-9227-67bad6a17edc'):
        await page.goto("http://localhost:4400/__ap/frame?profile=laptop-1280&run=r7-laptop-1280__checkout&start=%2F%23shop")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Add to cart for Trail Runner Shoes', instruction_id='799cd1b3-d4f2-4838-930b-0d32821ccd2f'):
        _loc_2 = frame_0.locator("internal:role=article >> internal:has-text=\"Trail Runner Shoes $129.00\"i >> internal:role=button")
        
        await _loc_2.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the header navigation links are visible'):
        set_var('header_navigation_links_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(5).querySelectorAll('a')).some(a => { const s = getComputedStyle(a); return s.display !== 'none' && s.visibility !== 'hidden' && s.opacity !== '0' && a.getClientRects().length > 0; }));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Home Shop Cart (1)"i'], query='whether the header navigation links in the site banner are visible', expected_value='false', needs_unit_conversion=False, operator='equals', transforms=[], condition="The site's header navigation links are not visible."))
    if await testmu.evaluate_branch(sub_checks=[{'description': "The site's header navigation links are not visible.", 'store_key': 'header_navigation_links_visible', 'expected_value': 'false', 'stored_value': '{{header_navigation_links_visible}}', 'extracted_value': '{{header_navigation_links_visible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        page = await testmu.execute_kane_cli('open the Menu button', page=page)
    frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking the Cart link in the header navigation', instruction_id='2bd4e3b1-0c18-4b1c-a722-385c2a017538'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Cart (1)\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Waiting for the order to be placed', instruction_id='ed582467-3a3a-4ffd-af26-e0a00b23840b'):
        await page.wait_for_timeout(1000)
        frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "2" into "Quantity for Trail Runner Shoes"', instruction_id='d981c2fe-61a4-41f8-ac22-fe0528ef4edc'):
        element_0 = frame_4.locator("internal:role=spinbutton[name=\"Quantity for Trail Runner\"i]")
        
        await testmu.fill(element_0, "2")
        # Reset to main page context
        frame_5 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Place order button', instruction_id='ff8b4e0c-17fc-4e8d-a777-a888a1f6c1f8'):
        _loc_7 = frame_5.locator("internal:role=button[name=\"Place order\"i]")
        
        await _loc_7.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the order confirmation message is present'):
        set_var('order_confirmed_message_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/Order confirmed/i.test(el(12).innerText));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Order confirmed! 2 items, $"i'], query="whether an 'Order confirmed' message is present in the order status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="An 'Order confirmed' message appears."))
    
    async with testmu.step('Assertion check', instruction_id='f1a95558-2834-4d74-bb58-600b8bc3885f'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "An 'Order confirmed' message appears.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{order_confirmed_message_visible}}', 'store_key': 'order_confirmed_message_visible', 'variable_refs': {'{{order_confirmed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "An 'Order confirmed' message appears.", 'store_key': 'order_confirmed_message_visible', 'expected_value': 'true', 'extracted_value': '{{order_confirmed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "An 'Order confirmed' message appears."})
    
    async with testmu.step('Reading the session issue count from the AspectProof layout panel'):
        set_var('aspectproof_layout_issues_seen_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(20).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['#ap-seen'], query='the Issues seen this session value in the AspectProof layout panel', expected_value='0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Extracting the full AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {16: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(16).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='ff1c7837-c3fe-48fe-91ac-a81c472cf33c'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '0', 'extracted_value': '{{aspectproof_layout_issues_seen_session}}', 'store_key': 'aspectproof_layout_issues_seen_session', 'variable_refs': {'{{aspectproof_layout_issues_seen_session}}': '0'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'aspectproof_layout_issues_seen_session', 'expected_value': '0', 'extracted_value': '{{aspectproof_layout_issues_seen_session}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)