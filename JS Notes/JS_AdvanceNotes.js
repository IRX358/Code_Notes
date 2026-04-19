// JavaScript Advanced notes with code from here
//JS needs runtime environments to run locally without browser like "Node js" "Deno" "Bun"
// Here using Node Js ---> To run your .js file use 'node filename.js'
//ANCHOR To run one particular snippet select it and then "ctrl+r r" , if not selected then entire file will run (Code runner extention to be installed)


// A sample html file is created for DOM manipulation (DOM_Manipulation_Sample.html)
//NOTE 1] __DOM________
// DOM (Document Object Model) is a programming interface that allows JavaScript to access and manipulate HTML documents
// DOM represents the document as a tree of objects (nodes) where each node is part of the document

// DOM Tree Structure:
// Document (root)
//   ├── html
//       ├── head
//       │   ├── title
//       │   ├── meta
//       │   └── link
//       └── body
//           ├── div
//           ├── p
//           ├── a
//           └── ...

// Accessing DOM elements
// 1. getElementById - returns single element
const headerElement = document.getElementById('header');

// 2. getElementsByClassName - returns HTMLCollection (live)
const buttons = document.getElementsByClassName('btn');

// 3. getElementsByTagName - returns HTMLCollection (live)
const paragraphs = document.getElementsByTagName('p');

// 4. querySelector - returns first matching element (static)
const firstButton = document.querySelector('.btn');

// 5. querySelectorAll - returns NodeList (static)
const allButtons = document.querySelectorAll('.btn');

console.log('First button:', firstButton);
console.log('All buttons:', allButtons);

// ___DOM Element Manipulation____________

// Creating elements
const newDiv = document.createElement('div');
newDiv.id = 'newDiv';
newDiv.className = 'container';
newDiv.textContent = 'This is a new div';

// Adding content
newDiv.innerHTML = '<strong>Bold text</strong> and <em>italic text</em>';
newDiv.innerText = 'Text content only (no HTML)';

// Appending elements
document.body.appendChild(newDiv);

// Inserting elements at specific positions
const parent = document.querySelector('.parent');
const child = document.createElement('p');
parent.insertBefore(child, parent.firstChild); // Insert before first child
parent.append(child); // Insert as last child
parent.prepend(child); // Insert as first child

// Removing elements
const elementToRemove = document.getElementById('removeMe');
elementToRemove.remove(); // Modern method
// or
parent.removeChild(elementToRemove); // Older method

// Replacing elements
const newElement = document.createElement('span');
parent.replaceChild(newElement, elementToRemove);

// Cloning elements
const clonedDiv = newDiv.cloneNode(true); // true = deep clone (with children)
const shallowClone = newDiv.cloneNode(false); // false = shallow clone (without children)

console.log('Cloned element:', clonedDiv);

// ___DOM Traversal____________

// Parent, Child, Sibling navigation
const element = document.querySelector('.my-element');

// Parent navigation
const parentElement = element.parentElement;
const parentNode = element.parentNode; // includes document and document fragment

// Child navigation
const firstChild = element.firstElementChild; // First element child
const lastChild = element.lastElementChild; // Last element child
const children = element.children; // HTMLCollection of element children
const childNodes = element.childNodes; // NodeList of all nodes (including text, comments)

// Sibling navigation
const nextSibling = element.nextElementSibling; // Next element sibling
const previousSibling = element.previousElementSibling; // Previous element sibling
const nextNode = element.nextSibling; // Next node (including text, comments)
const previousNode = element.previousSibling; // Previous node

// Walking the DOM tree
function walkDOM(node, depth = 0) {
    console.log('  '.repeat(depth) + node.nodeName);
    
    for (let i = 0; i < node.childNodes.length; i++) {
        walkDOM(node.childNodes[i], depth + 1);
    }
}

// ___DOM Styling and CSS Manipulation____________

// Inline styles
const box = document.querySelector('.box');
box.style.backgroundColor = 'red';
box.style.color = 'white';
box.style.fontSize = '20px';
box.style.padding = '10px';

// Working with CSS classes
box.classList.add('highlight');
box.classList.remove('highlight');
box.classList.toggle('active');
box.classList.contains('active'); // returns boolean
box.classList.replace('old-class', 'new-class');

// Multiple classes
box.classList.add('class1', 'class2', 'class3');

// Getting computed styles
const computedStyle = window.getComputedStyle(box);
console.log('Background color:', computedStyle.backgroundColor);
console.log('Font size:', computedStyle.fontSize);

// CSS variables (custom properties)
document.documentElement.style.setProperty('--primary-color', '#3498db');
const primaryColor = getComputedStyle(document.documentElement).getPropertyValue('--primary-color');

// ___DOM Attributes and Properties____________

// Getting and setting attributes
const link = document.querySelector('a');
link.getAttribute('href'); // Get attribute
link.setAttribute('href', 'https://example.com'); // Set attribute
link.removeAttribute('target'); // Remove attribute
link.hasAttribute('href'); // Check if attribute exists

// Data attributes
const userElement = document.querySelector('[data-user-id]');
const userId = userElement.dataset.userId; // Get data-user-id
userElement.dataset.userId = '123'; // Set data-user-id

// Common attributes
inputElement.value = 'New value'; // Form input value
inputElement.checked = true; // Checkbox/radio
inputElement.disabled = true; // Disable element
imgElement.src = 'new-image.jpg';
imgElement.alt = 'Description';

// Properties vs Attributes
// Properties are the current state of the DOM element
// Attributes are the initial HTML values
const checkbox = document.querySelector('input[type="checkbox"]');
checkbox.checked = true; // Property (current state)
checkbox.setAttribute('checked', 'checked'); // Attribute (initial value)

//___DOM Event Handling____________

// Event listeners
const button = document.querySelector('.click-btn');

button.addEventListener('click', function(event) {
    console.log('Button clicked!');
    console.log('Event object:', event);
});

// Arrow function for event listener
button.addEventListener('click', (event) => {
    console.log('Arrow function handler');
    console.log('Event target:', event.target);
});

// Event listener with options
button.addEventListener('click', handler, {
    capture: true, // Use capture phase instead of bubbling
    once: true, // Remove listener after first call
    passive: true // Improves scroll performance
});

// Removing event listeners
function handler(event) {
    console.log('Handler called');
}

button.addEventListener('click', handler);
button.removeEventListener('click', handler);

// Event object properties
button.addEventListener('click', (event) => {
    console.log('Event type:', event.type);
    console.log('Event target:', event.target);
    console.log('Current target:', event.currentTarget);
    console.log('Client X:', event.clientX);
    console.log('Client Y:', event.clientY);
    console.log('Key pressed:', event.key);
    console.log('Prevent default:', event.preventDefault());
    console.log('Stop propagation:', event.stopPropagation());
});

// Common events
element.addEventListener('click', handler); // Click event
element.addEventListener('dblclick', handler); // Double click
element.addEventListener('mouseover', handler); // Mouse over
element.addEventListener('mouseout', handler); // Mouse out
element.addEventListener('mousemove', handler); // Mouse move
element.addEventListener('keydown', handler); // Key down
element.addEventListener('keyup', handler); // Key up
element.addEventListener('change', handler); // Form change
element.addEventListener('submit', handler); // Form submit
element.addEventListener('focus', handler); // Element focus
element.addEventListener('blur', handler); // Element blur
element.addEventListener('load', handler); // Page/element loaded
element.addEventListener('resize', handler); // Window resize
element.addEventListener('scroll', handler); // Scroll event

// Event delegation (performance optimization)
document.addEventListener('click', function(event) {
    if (event.target.matches('.dynamic-button')) {
        console.log('Dynamic button clicked:', event.target);
    }
});

//_____DOM Forms and Input Handling____________

// Form selection
const form = document.querySelector('#myForm');
const inputs = form.querySelectorAll('input');

// Form submission
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
    
    // Get form data
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    console.log('Form data:', data);
    
    // Alternative: manual collection
    const name = form.querySelector('#name').value;
    const email = form.querySelector('#email').value;
    console.log('Name:', name, 'Email:', email);
});

// Input validation
const emailInput = document.querySelector('#email');
emailInput.addEventListener('input', function() {
    if (!emailInput.value.includes('@')) {
        emailInput.style.borderColor = 'red';
    } else {
        emailInput.style.borderColor = 'green';
    }
});

// Form reset
form.reset();

//___DOM Animation and Transitions____________

// CSS transitions (preferred for simple animations)
const animatedBox = document.querySelector('.animated-box');
animatedBox.style.transition = 'all 0.3s ease';

animatedBox.addEventListener('mouseover', function() {
    this.style.transform = 'scale(1.1)';
    this.style.backgroundColor = 'blue';
});

animatedBox.addEventListener('mouseout', function() {
    this.style.transform = 'scale(1)';
    this.style.backgroundColor = 'red';
});

// CSS animations with JavaScript
animatedBox.style.animation = 'fadeIn 1s ease-in-out';

// RequestAnimationFrame for smooth animations
function animate() {
    const box = document.querySelector('.moving-box');
    let position = 0;
    
    function step() {
        position += 1;
        box.style.left = position + 'px';
        
        if (position < 300) {
            requestAnimationFrame(step);
        }
    }
    
    requestAnimationFrame(step);
}

// ___DOM Storage (Local and Session)____________

// LocalStorage (persists even after browser close)
localStorage.setItem('username', 'John');
const username = localStorage.getItem('username');
localStorage.removeItem('username');
localStorage.clear(); // Clear all items

// Storing objects (need to stringify)
const user = { name: 'John', age: 30 };
localStorage.setItem('user', JSON.stringify(user));
const storedUser = JSON.parse(localStorage.getItem('user'));

// SessionStorage (clears when tab closes)
sessionStorage.setItem('tempData', 'temporary');
const tempData = sessionStorage.getItem('tempData');




//NOTE 2] __    ________
//NOTE 3] __    ________
//NOTE 4] __    ________
//NOTE 5] __    ________
//NOTE 6] __    ________
//NOTE 7] __    ________
//NOTE 8] __    ________
//NOTE 9] __    ________
//NOTE 10] __    ________