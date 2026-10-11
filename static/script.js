function toggleMobileMenu() {
  document.body.classList.toggle('mobile-menu-active');
}

function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
  }
}

// Program Filter Tabs
function filterPrograms(category, btnElement) {
  const buttons = document.querySelectorAll('.tab-btn');
  buttons.forEach(btn => btn.classList.remove('active'));
  if (btnElement) {
    btnElement.classList.add('active');
  }

  const cards = document.querySelectorAll('#programsGrid .program-card');
  cards.forEach(card => {
    const cardCat = card.getAttribute('data-category');
    if (category === 'all' || cardCat === category) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });
}

// ==========================================
// 2. MODALS CONTROLLER
// ==========================================

function openAdmissionsModal(courseName = '') {
  const modal = document.getElementById('admissionsModal');
  const courseInput = document.getElementById('modalCourseInput');
  if (courseInput && courseName) {
    courseInput.value = courseName;
  }
  if (modal) {
    modal.classList.add('active');
  }
}

function closeAdmissionsModal() {
  const modal = document.getElementById('admissionsModal');
  if (modal) {
    modal.classList.remove('active');
  }
}

function handleModalSubmit(event) {
  event.preventDefault();
  alert('Thank you for registering your interest! The NCERC Admissions Office will contact you.');
  closeAdmissionsModal();
}

function handleContactSubmit(event) {
  event.preventDefault();
  alert('Your enquiry has been received by NCERC Administration. We will respond via phone/email.');
  event.target.reset();
}

// Department Details Modal Data
const deptData = {
  mct: {
    title: 'Department of Mechatronics Engineering',
    badge: 'NBA Accredited UG Programme',
    hod: 'Faculty Division Head',
    description: 'Interdisciplinary domain integrating mechanical systems, electronics, control algorithms, and industrial robotics automation.',
    labs: ['Robotics & Industrial Automation Workshop', 'Pneumatics & Hydraulics Lab', 'PLC Programming Center'],
    courses: 'B.Tech Mechatronics Engineering (4 Years)'
  },
  cse: {
    title: 'Department of Computer Science & Engineering',
    badge: 'NBA Accredited UG Programme',
    hod: 'Faculty Division Head',
    description: 'Focuses on software engineering, algorithm design, cloud computing, cybersecurity, and system architecture.',
    labs: ['High Performance Computing Center', 'Software Engineering Studio', 'Systems & Networking Lab'],
    courses: 'B.Tech CSE (4 Years) | M.Tech CSE (2 Years)'
  },
  aiml: {
    title: 'Department of CSE (AI & Machine Learning)',
    badge: 'Approved Specialized Branch',
    hod: 'Faculty Division Head',
    description: 'Specialized focus on neural networks, deep learning models, natural language processing, and computer vision systems.',
    labs: ['AI Research Hub', 'Data Analytics Studio', 'GPU Accelerator Center'],
    courses: 'B.Tech CSE (AI & ML) (4 Years)'
  },
  ece: {
    title: 'Department of Electronics & Communication',
    badge: 'NBA Accredited UG Programme',
    hod: 'Faculty Division Head',
    description: 'Provides technical training in VLSI circuit design, embedded microcontrollers, signal processing, and wireless networks.',
    labs: ['VLSI Design Center', 'Embedded Systems & Robotics Studio', 'DSP & Microwave Lab'],
    courses: 'B.Tech ECE (4 Years) | M.Tech VLSI Design (2 Years)'
  },
  eee: {
    title: 'Department of Electrical & Electronics Engineering',
    badge: 'KTU Affiliated',
    hod: 'Faculty Division Head',
    description: 'Covers electrical power systems, power electronics, industrial control, and renewable energy conversion.',
    labs: ['Electrical Machines Lab', 'Power Electronics Studio', 'Control Systems Lab'],
    courses: 'B.Tech EEE (4 Years)'
  },
  me: {
    title: 'Department of Mechanical Engineering',
    badge: 'KTU Affiliated',
    hod: 'Faculty Division Head',
    description: 'Provides training in thermal science, manufacturing processes, CAD/CAM design, and material mechanics.',
    labs: ['CAD/CAM Computing Studio', 'Thermal Engineering Lab', 'Material Testing Center'],
    courses: 'B.Tech Mechanical Engineering (4 Years)'
  },
  mtech: {
    title: 'Postgraduate M.Tech Programmes',
    badge: 'Postgraduate Division',
    hod: 'PG Coordinator',
    description: 'Master of Technology degrees in Computer Science & Engineering, Cyber Security, Energy Systems, and VLSI Design.',
    labs: ['PG Advanced Research Studios'],
    courses: 'M.Tech CSE | M.Tech Cyber Security | M.Tech Energy Systems | M.Tech VLSI'
  },
  mca: {
    title: 'Department of Computer Applications (MCA)',
    badge: 'NBA Accredited PG Programme',
    hod: 'Faculty Division Head',
    description: 'Postgraduate software degree covering cloud infrastructure, web architecture, mobile applications, and database administration.',
    labs: ['Advanced Software Application Lab', 'Web Technologies Center'],
    courses: 'MCA (2 Years)'
  },
  mba: {
    title: 'Department of Business Administration (MBA)',
    badge: 'Postgraduate Management Division',
    hod: 'Faculty Division Head',
    description: 'Postgraduate management degree with specializations in Finance, Systems, Human Resource, Marketing, and Operations.',
    labs: ['Management Decision Studio', 'Business Analytics Hub'],
    courses: 'MBA (2 Years)'
  }
};

function showDeptDetails(deptKey) {
  const data = deptData[deptKey];
  if (!data) return;

  const contentBox = document.getElementById('deptModalContent');
  contentBox.innerHTML = `
    <span class="badge badge-burgundy" style="margin-bottom: 12px;">${data.badge}</span>
    <h2 style="font-size: 1.25rem; font-weight: 800; color: var(--ncerc-navy); margin-bottom: 8px;">${data.title}</h2>
    <p style="font-size: 0.875rem; font-weight: 700; color: var(--ncerc-burgundy); margin-bottom: 16px;">${data.hod}</p>
    <p style="font-size: 0.9375rem; color: var(--color-text-muted); line-height: 1.6; margin-bottom: 20px;">${data.description}</p>
    
    <h4 style="font-size: 0.9375rem; font-weight: 700; color: var(--ncerc-navy); margin-bottom: 8px;">Department Facilities:</h4>
    <ul style="list-style: disc; margin-left: 20px; font-size: 0.875rem; color: var(--color-text-muted); margin-bottom: 20px;">
      ${data.labs.map(lab => `<li>${lab}</li>`).join('')}
    </ul>
    
    <p style="font-size: 0.8125rem; background: var(--color-bg-light); padding: 10px; border-left: 3px solid var(--ncerc-navy);"><strong>Degree Offerings:</strong> ${data.courses}</p>
    <div style="margin-top: 24px; text-align: right;">
      <button class="btn btn-primary btn-sm" onclick="openAdmissionsModal('${data.title}'); closeDeptModal();">Inquire for Department</button>
    </div>
  `;

  document.getElementById('deptModal').classList.add('active');
}

function closeDeptModal() {
  document.getElementById('deptModal').classList.remove('active');
}

window.addEventListener('click', function(e) {
  const admissionsModal = document.getElementById('admissionsModal');
  const deptModal = document.getElementById('deptModal');
  if (e.target === admissionsModal) closeAdmissionsModal();
  if (e.target === deptModal) closeDeptModal();
});

// ==========================================
// 3. CHATBOT CONTROLLER & ANIMATION STATE
// ==========================================

function toggleChatbot() {
  const panel = document.getElementById('chatbotPanel');
  const launcher = document.getElementById('chatbotLauncher');
  
  if (panel) {
    const isActive = panel.classList.toggle('active');
    
    // Toggle class on launcher to pause/resume infinite wave animation
    if (launcher) {
      if (isActive) {
        launcher.classList.add('panel-open');
      } else {
        launcher.classList.remove('panel-open');
      }
    }
  }
}

function selectSuggestedQuestion(questionText) {
  const chatInput = document.getElementById('chatInput');
  if (chatInput) {
    chatInput.value = questionText;
    chatInput.focus();
  }
}

function handleChatSubmit(event) {
  event.preventDefault();
  const input = document.getElementById('chatInput');
  const query = input.value.trim();
  if (!query) return;

  // Hide initial welcome greeting upon first message
  const emptyState = document.getElementById('chatEmptyState');
  if (emptyState) {
    emptyState.style.display = 'none';
  }

  // ONLY display the user's message in the conversation area
  appendUserMessage(query);
  input.value = '';

  // Architecture Hook for Future Flask API Backend Integration
  // Backend is exposed as window.NCERCAssistantBackend and remains compatible with the older name.
  const backend = window.NCERCAssistantBackend || window.NCERCassistantBackend;
  if (backend && typeof backend.submitQuery === 'function') {
    backend.submitQuery(query, function(backendResponseHTML) {
      if (backendResponseHTML) {
        appendAssistantMessage(backendResponseHTML);
      }
    });
  } else {
    appendAssistantMessage('Sorry, the chatbot backend is not available right now.');
  }
}

function appendUserMessage(text) {
  const chatBody = document.getElementById('chatBody');
  const msgDiv = document.createElement('div');
  msgDiv.className = 'chat-msg chat-msg-user';
  msgDiv.innerHTML = `
    <span class="msg-sender">You</span>
    <div class="msg-bubble"><p>${escapeHTML(text)}</p></div>
  `;
  chatBody.appendChild(msgDiv);
  chatBody.scrollTop = chatBody.scrollHeight;
}

function appendAssistantMessage(htmlText) {
  const chatBody = document.getElementById('chatBody');
  const msgDiv = document.createElement('div');
  msgDiv.className = 'chat-msg chat-msg-assistant';
  msgDiv.innerHTML = `
    <span class="msg-sender">College Assistant</span>
    <div class="msg-bubble">${htmlText}</div>
  `;
  chatBody.appendChild(msgDiv);
  chatBody.scrollTop = chatBody.scrollHeight;
}

function escapeHTML(str) {
  return str.replace(/[&<>'"]/g, 
    tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
  );
}

/* 
   Future Backend Architecture Hook
   Flask API Connection Endpoint Handle:
   User Message -> Frontend -> Flask Backend -> AI/NLP -> SQL Database -> Verified NCERC Info -> Response
   (Currently empty until Flask backend is connected)
*/
window.NCERCAssistantBackend = {
    submitQuery: function(queryText, callback) {
        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: queryText
            })
        })
        .then(function(response) {
            if (!response.ok) {
                throw new Error("Server error");
            }
            return response.json();
        })
        .then(function(data) {
            callback(data && data.response ? data.response : 'No response received.');
        })
        .catch(function(error) {
            console.error("Chatbot error:", error);
            callback("Sorry, I'm having trouble connecting right now. Please try again.");
        });
    }
};

window.NCERCassistantBackend = window.NCERCAssistantBackend;
