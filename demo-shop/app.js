// Northtrail Outfitters — tiny hash-routed demo shop for AspectProof.
const PRODUCTS = [
  { id: 'trail-runner', name: 'Trail Runner Shoes', price: 129.0, color: '#c9d8c5' },
  { id: 'daypack-22', name: 'Daypack 22L', price: 89.0, color: '#e6d3b3' },
  { id: 'storm-shell', name: 'Storm Shell Jacket', price: 189.0, color: '#b9c7d6' },
  { id: 'merino-tee', name: 'Merino Trail Tee', price: 59.0, color: '#ddc6c6' },
];

const cart = new Map(); // id -> qty
const $ = (sel) => document.querySelector(sel);
const money = (n) => `$${n.toFixed(2)}`;

function renderProducts() {
  $('#product-grid').innerHTML = PRODUCTS.map((p) => `
    <article class="product" data-id="${p.id}">
      <div class="swatch" style="background:${p.color}"></div>
      <h3>${p.name}</h3>
      <div class="price">${money(p.price)}</div>
      <button class="btn add-to-cart" data-id="${p.id}">Add to cart</button>
    </article>`).join('');
}

function renderCart() {
  const count = [...cart.values()].reduce((a, b) => a + b, 0);
  $('#cart-count').textContent = String(count);
  const items = [...cart.entries()].map(([id, qty]) => ({ ...PRODUCTS.find((p) => p.id === id), qty }));
  $('#cart-empty').hidden = items.length > 0;
  $('#cart-contents').hidden = items.length === 0;
  $('#cart-items').innerHTML = items.map((it) => `
    <li class="cart-item" data-id="${it.id}">
      <span>${it.name}</span>
      <label>Qty <input type="number" min="1" value="${it.qty}" data-id="${it.id}" class="qty" aria-label="Quantity for ${it.name}"></label>
      <strong>${money(it.price * it.qty)}</strong>
    </li>`).join('');
  const subtotal = items.reduce((s, it) => s + it.price * it.qty, 0);
  const shipping = subtotal === 0 || subtotal >= 75 ? 0 : 8;
  $('#cart-subtotal').textContent = money(subtotal);
  $('#cart-shipping').textContent = shipping ? money(shipping) : 'Free';
  $('#cart-total').textContent = money(subtotal + shipping);
}

function show(view) {
  for (const v of document.querySelectorAll('.view')) v.hidden = v.id !== `view-${view}`;
  $('#site-nav').classList.remove('open');
  $('.menu-toggle').setAttribute('aria-expanded', 'false');
  window.scrollTo(0, 0);
}

function route() {
  const view = (location.hash || '#home').slice(1);
  show(['home', 'shop', 'cart'].includes(view) ? view : 'home');
}

document.addEventListener('click', (e) => {
  const add = e.target.closest('.add-to-cart');
  if (add) {
    const id = add.dataset.id;
    cart.set(id, (cart.get(id) || 0) + 1);
    $('#order-confirmation').hidden = true;
    renderCart();
    add.textContent = 'Added ✓';
    setTimeout(() => { add.textContent = 'Add to cart'; }, 1200);
  }
  if (e.target.closest('.menu-toggle')) {
    const open = $('#site-nav').classList.toggle('open');
    $('.menu-toggle').setAttribute('aria-expanded', String(open));
  }
  if (e.target.closest('.promo-close')) {
    $('.promo-bar').hidden = true;
  }
  if (e.target.closest('#place-order')) {
    const n = [...cart.values()].reduce((a, b) => a + b, 0);
    const total = $('#cart-total').textContent;
    cart.clear();
    renderCart();
    const conf = $('#order-confirmation');
    conf.textContent = `Order confirmed! ${n} item${n === 1 ? '' : 's'}, ${total} total. Order #NT-${Math.floor(1000 + Math.random() * 9000)}.`;
    conf.hidden = false;
  }
});

document.addEventListener('change', (e) => {
  if (e.target.matches('.qty')) {
    const qty = Math.max(1, parseInt(e.target.value, 10) || 1);
    cart.set(e.target.dataset.id, qty);
    renderCart();
  }
});

$('#signup-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const form = e.target;
  const name = form.name.value.trim();
  const email = form.email.value.trim();
  const msg = $('#signup-message');
  msg.hidden = false;
  if (!name || !/^\S+@\S+\.\S+$/.test(email)) {
    msg.textContent = 'Please enter your name and a valid email.';
    msg.className = 'message';
    return;
  }
  msg.textContent = `Thanks, ${name}! You're subscribed.`;
  msg.className = 'message success';
  form.reset();
});

window.addEventListener('hashchange', route);
renderProducts();
renderCart();
route();
