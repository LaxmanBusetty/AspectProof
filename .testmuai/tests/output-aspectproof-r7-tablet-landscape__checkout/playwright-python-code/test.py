import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="d4970d1a-6b71-4503-88d3-ec12851a5a87",
    name="Add Trail Runner Shoes to Cart and Place Order",
    tc_id="TC-72",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"header_navigation_links_visible": "true", "order_confirmed_message_visible": "true", "aspectproof_issues_seen_this_session": "0", "layout_report": "AspectProof layout\nTablet landscape 1024\u00d7768 (full window)\nProbe: active (158 scans)\nIssues now: 0\nIssues seen this session: 0"},
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to http://localhost:4400/__ap/frame?profile=tablet-landscape&run=r7-tablet-landscape__checkout&start=%2F%23shop', instruction_id='40d26869-5b01-4634-a12b-3f6a593f2dd0'):
        await page.goto("http://localhost:4400/__ap/frame?profile=tablet-landscape&run=r7-tablet-landscape__checkout&start=%2F%23shop")
        frame_0 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Add to cart for Trail Runner Shoes', instruction_id='739305a6-a5d6-42e3-8991-2237648b026f'):
        _loc_2 = frame_0.locator("internal:role=article >> internal:has-text=\"Trail Runner Shoes $129.00\"i >> internal:role=button")
        
        await _loc_2.click()
        # Reset to main page context
    
    async with testmu.step('Checking whether the header navigation links are visible'):
        set_var('header_navigation_links_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {5: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (Array.from(el(5).querySelectorAll('a')).some(a => !!(a.offsetWidth || a.offsetHeight || a.getClientRects().length) && getComputedStyle(a).visibility !== 'hidden' && getComputedStyle(a).display !== 'none'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Home Shop Cart (1)"i'], query="whether the header navigation links in the site's header are visible", expected_value='false', needs_unit_conversion=False, operator='equals', transforms=[], condition="the site's header navigation links are not visible"))
    if await testmu.evaluate_branch(sub_checks=[{'description': "the site's header navigation links are not visible", 'store_key': 'header_navigation_links_visible', 'expected_value': 'false', 'stored_value': '{{header_navigation_links_visible}}', 'extracted_value': '{{header_navigation_links_visible}}', 'operator': 'equals', 'transforms': []}], composite_operator="and"):
        page = await testmu.execute_kane_cli('open the Menu button first', page=page)
    frame_2 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Opening the cart from the header navigation Cart 1 link', instruction_id='309bfde8-f814-42fc-baee-46922ceb47d5'):
        _loc_4 = frame_2.locator("internal:role=link[name=\"Cart (1)\"i]")
        
        await _loc_4.click()
        # Reset to main page context
    
    async with testmu.step('Waiting for plan to process steps in the queue', instruction_id='7e31e705-dd82-42f5-a94d-afd03ad0f3fd'):
        await page.wait_for_timeout(1000)
        frame_4 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Type "2" into "Quantity for Trail Runner Shoes"', instruction_id='b320b16a-58a1-412d-8394-1822c975ee6d'):
        element_0 = frame_4.locator("internal:role=spinbutton[name=\"Quantity for Trail Runner\"i]")
        
        await testmu.fill(element_0, "2")
        # Reset to main page context
        frame_5 = page.frame_locator("iframe[title=\"App under test\"]")
    
    async with testmu.step('Clicking Place order button', instruction_id='d4c42a22-b567-407b-936f-6a5db322fd49'):
        _loc_7 = frame_5.locator("internal:role=button[name=\"Place order\"i]")
        
        await _loc_7.click()
        # Reset to main page context
    _condition_met = False
    _until_retries = 0
    while _until_retries < 10:
        print(f"[until-loop] iteration {_until_retries + 1}/10")
        async with testmu.step('Waiting for the Order confirmed message to be visible', instruction_id='c34ca920-0f09-4375-bb9f-01ded5a3ae6f'):
            await page.wait_for_timeout(500)
        await page.wait_for_timeout(500)
        if await testmu.check_until_condition(page, "the text 'Order confirmed' is visible"):
            _condition_met = True
            break
        _until_retries += 1
    set_var("__result__", {"condition_met": _condition_met, "retries": _until_retries + 1})
    
    async with testmu.step('Checking whether the order confirmation message is present'):
        set_var('order_confirmed_message_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {12: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(12).innerText.includes('Order confirmed') && !!(el(12).offsetWidth || el(12).offsetHeight || el(12).getClientRects().length));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['iframe[title="App under test"] >> internal:control=enter-frame >> internal:text="Order confirmed! 2 items, $"i'], query="whether the 'Order confirmed' message in the order confirmation status region is present", expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition="an 'Order confirmed' message appears"))
    
    async with testmu.step('Assertion check', instruction_id='5162830d-0cdb-426c-bf5e-8ccd1bec7155'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': "an 'Order confirmed' message appears", 'passed': True, 'operator': 'equals', 'transforms': [], 'json_path': None, 'expected': 'true', 'extracted_value': '{{order_confirmed_message_visible}}', 'store_key': 'order_confirmed_message_visible', 'variable_refs': {'{{order_confirmed_message_visible}}': 'true'}}], 'sub_checks': [{'description': "an 'Order confirmed' message appears", 'store_key': 'order_confirmed_message_visible', 'expected_value': 'true', 'extracted_value': '{{order_confirmed_message_visible}}', 'operator': 'equals', 'transforms': []}], 'composite_operator': 'and', 'claim': "an 'Order confirmed' message appears"})
    
    async with testmu.step('Reading the session issue count from the AspectProof layout panel'):
        set_var('aspectproof_issues_seen_this_session', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {19: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(19).querySelector('strong')?.innerText.trim() ?? null);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="Issues seen this session:"i'], query='the Issues seen this session count in the AspectProof layout panel', expected_value='0', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the "AspectProof layout" panel shows "Issues seen this session: 0"'))
    
    async with testmu.step('Extracting the AspectProof layout panel text'):
        set_var('layout_report', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {16: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(16).innerText);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=complementary[name="AspectProof layout panel"i]'], query='the full text of the AspectProof layout panel', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the full panel text is stored as {{layout_report}}'))
    
    async with testmu.step('Assertion check', instruction_id='1ed153e0-b0b6-4486-ae26-b78ffb2e522b'):
        await testmu.verify_assertion(page, 'Assertion check', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_results': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'passed': True, 'operator': 'equals', 'transforms': ['strip'], 'json_path': None, 'expected': '0', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'store_key': 'aspectproof_issues_seen_this_session', 'variable_refs': {'{{aspectproof_issues_seen_this_session}}': '0'}}], 'sub_checks': [{'description': 'the "AspectProof layout" panel shows "Issues seen this session: 0"', 'store_key': 'aspectproof_issues_seen_this_session', 'expected_value': '0', 'extracted_value': '{{aspectproof_issues_seen_this_session}}', 'operator': 'equals', 'transforms': ['strip']}], 'composite_operator': 'and', 'claim': 'the "AspectProof layout" panel shows "Issues seen this session: 0"'})


if __name__ == "__main__":
    testmu.run(test)