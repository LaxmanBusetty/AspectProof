import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="84805c15-251c-4b3d-8099-f1b021686e99",
    name="Web || laxmanbusetty || TC-42",
    tc_id="TC-42",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"header_navigation_links_visible": "true", "order_confirmed_message": "true", "aspectproof_issues_seen_this_session": "true", "layout_report": "AspectProof layout\nTablet portrait 768\u00d71024 \u00b7 portrait\nProbe: active (100 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=tablet-portrait&run=r5-tablet-portrait__checkout&start=%2F%23shop', instruction_id='a2ce2756-ac14-48fc-a833-bc928502b17b'):
        await page.goto("http://localhost:4400/__ap/frame?profile=tablet-portrait&run=r5-tablet-portrait__checkout&start=%2F%23shop")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Add to cart for Trail Runner Shoes', instruction_id='d712539d-218d-4fc8-abab-3ca4c14b3b14'):
        _loc_2 = frame_0.locator("internal:role=article >> internal:has-text=\"Trail Runner Shoes $129.00\"i >> internal:role=button")
        
        await _loc_2.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the header navigation links are visible'):
        set_var('header_navigation_links_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(5).querySelectorAll('a')).some(a => { const s=getComputedStyle(a); const r=a.getBoundingClientRect(); return s.display !== 'none' && s.visibility !== 'hidden' && s.opacity !== '0' && r.width > 0 && r.height > 0; }));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Home Shop Cart (1)"i'], query='whether the header navigation links in the site banner are visible', expected_value='false', needs_unit_conversion=False, operator='equals', transforms=[], condition="the site's header navigation links are not visible"))
    if await testmu.evaluate_branch(sub_checks=[{'description': "the site's header navigation links are not visible", 'store_key': 'header_navigation_links_visible', 'expected_value': 'false', 'stored_value': '{{header_navigation_links_visible}}', 'extracted_value': '{{header_navigation_links_visible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        page = await testmu.execute_kane_cli('open the Menu button', page=page)
    frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Cart (1) in the header navigation', instruction_id='fe000ed6-78e4-4b9a-8a60-ef815a9069d8'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Cart (1)\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Waiting for the plan to complete', instruction_id='c4d3ce43-b9fb-4a42-a673-e23f3bb13513'):
        await page.wait_for_timeout(1000)
        frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "2" into "Quantity for Trail Runner Shoes"', instruction_id='fb86e082-bd6a-4037-8c50-1b7a90a2719d'):
        element_0 = frame_4.locator("internal:role=spinbutton[name=\"Quantity for Trail Runner\"i]")
        
        await testmu.fill(element_0, "2")
        # Reset to main page context
        frame_5 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Place order button', instruction_id='006c1ef3-8719-4ffb-bbbc-781ae44ef3cb'):
        _loc_7 = frame_5.locator("internal:role=button[name=\"Place order\"i]")
        
        await _loc_7.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the order confirmation message is present'):
        set_var('order_confirmed_message', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/Order confirmed/.test(el(12).innerText));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Order confirmed! 2 items, $"i'], query="whether an 'Order confirmed' message is present in the order status message", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="An 'Order confirmed' message appears."))
    
    async with testmu.step('Checking the AspectProof layout issue count'):
        set_var('aspectproof_issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {16: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (/Issues seen this session:\\s*0/.test(el(16).innerText));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='whether "Issues seen this session: 0" is present in the "AspectProof layout" panel', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='The "AspectProof layout" panel shows "Issues seen this session: 0".'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {16: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(16).innerText.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the "AspectProof layout" panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='The full "AspectProof layout" panel text is stored as {{layout_report}}.'))
    
    async with testmu.step('Assertion check', instruction_id='b6fc164f-92d8-4973-8dbb-57ea48cf5562'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "An 'Order confirmed' message appears.", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{order_confirmed_message}}', 'store_key': 'order_confirmed_message', 'variable_refs': {'{{order_confirmed_message}}': 'true'}}], 'sub_checks': [{'description': "An 'Order confirmed' message appears.", 'store_key': 'order_confirmed_message', 'expected_value': 'true', 'extracted_value': '{{order_confirmed_message}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "An 'Order confirmed' message appears."})
    
    async with testmu.step('Assertion check', instruction_id='ec26a578-688a-4e5e-9c44-ca3d6e80fd6c'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'store_key': 'aspectproof_issues_seen_this_session', 'variable_refs': {'{{aspectproof_issues_seen_this_session}}': 'true'}}], 'sub_checks': [{'description': 'The "AspectProof layout" panel shows "Issues seen this session: 0".', 'store_key': 'aspectproof_issues_seen_this_session', 'expected_value': 'true', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': 'The "AspectProof layout" panel shows "Issues seen this session: 0".'})


if __name__ == "__main__":
    testmu.run(test)