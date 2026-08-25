import { useEffect, useState } from "react";
import "./App.css";

const API_BASE_URL = "http://127.0.0.1:8000";

const navigation = [
  { id: "dashboard", label: "Dashboard", icon: "⌂" },
  { id: "courses", label: "Courses", icon: "▣" },
  { id: "assessments", label: "Assessments", icon: "✓" },
  { id: "employees", label: "Employees", icon: "♙" },
  { id: "candidates", label: "Candidates", icon: "◉" },
  { id: "analytics", label: "Analytics", icon: "↗" },
];

function App() {
  const [activePage, setActivePage] = useState("dashboard");

  return (
    <div className="app">
      {/* SIDEBAR */}
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark">AI</div>

          <div>
            <h1>AI Tutor</h1>
            <span>Enterprise Learning</span>
          </div>
        </div>

        <div className="workspace">
          <span>WORKSPACE</span>
          <strong>Acme Organization</strong>
        </div>

        <nav className="navigation">
          {navigation.map((item) => (
            <button
              key={item.id}
              className={`nav-item ${
                activePage === item.id ? "active" : ""
              }`}
              onClick={() => setActivePage(item.id)}
            >
              <span className="nav-icon">{item.icon}</span>
              {item.label}
            </button>
          ))}
        </nav>

        <div className="sidebar-bottom">
          <button className="nav-item">
            <span className="nav-icon">⚙</span>
            Settings
          </button>

          <div className="user-card">
            <div className="avatar">JJ</div>

            <div>
              <strong>Jonathan James</strong>
              <span>Administrator</span>
            </div>

            <span className="more">•••</span>
          </div>
        </div>
      </aside>

      {/* MAIN CONTENT */}
      <main className="main">
        <header className="topbar">
          <div>
            <p className="eyebrow">AI TUTOR 2.0</p>
            <h2>{getPageTitle(activePage)}</h2>
          </div>

          <div className="top-actions">
            <button className="icon-button">⌕</button>
            <button className="icon-button notification">◔</button>

            <div className="top-avatar">JJ</div>
          </div>
        </header>

        {activePage === "dashboard" && <Dashboard />}

        {activePage === "courses" && <CoursesPage />}

        {activePage === "employees" && <EmployeesPage />}

        {activePage !== "dashboard" &&
          activePage !== "courses" &&
          activePage !== "employees" && (
            <PlaceholderPage title={getPageTitle(activePage)} />
          )}
      </main>
    </div>
  );
}

/* =========================================================
   DASHBOARD
========================================================= */

function Dashboard() {
  return (
    <div className="content">
      <section className="hero">
        <div>
          <span className="status-badge">● SYSTEM ONLINE</span>

          <h3>
            Good morning, Jonathan.
            <br />
            <span>Let's build better talent.</span>
          </h3>

          <p>
            Monitor employee development, evaluate candidates, and build
            high-performing teams from one intelligent learning platform.
          </p>

          <div className="hero-actions">
            <button className="primary-button">
              Explore courses →
            </button>

            <button className="secondary-button">
              View assessments
            </button>
          </div>
        </div>

        <div className="hero-orb">
          <div className="orb-core">AI</div>
          <div className="orb-ring ring-one"></div>
          <div className="orb-ring ring-two"></div>
        </div>
      </section>

      <section className="metrics">
        <Metric
          label="Active employees"
          value="248"
          change="+12.4%"
          icon="♙"
        />

        <Metric
          label="Candidates evaluated"
          value="86"
          change="+8.7%"
          icon="◉"
        />

        <Metric
          label="Average skill score"
          value="82%"
          change="+5.2%"
          icon="↗"
        />

        <Metric
          label="Courses completed"
          value="1,426"
          change="+18.9%"
          icon="✓"
        />
      </section>

      <section className="dashboard-grid">
        <div className="panel large-panel">
          <div className="panel-header">
            <div>
              <span className="panel-label">
                LEARNING DEVELOPMENT
              </span>

              <h3>Skill development overview</h3>
            </div>

            <button className="small-button">
              Last 30 days ▾
            </button>
          </div>

          <div className="chart">
            <div className="chart-y">
              <span>100</span>
              <span>75</span>
              <span>50</span>
              <span>25</span>
              <span>0</span>
            </div>

            <div className="chart-area">
              <div className="grid-line"></div>
              <div className="grid-line"></div>
              <div className="grid-line"></div>
              <div className="grid-line"></div>

              <div className="chart-bars">
                {[42, 55, 48, 67, 61, 75, 82, 71, 88, 94].map(
                  (height, index) => (
                    <div className="bar-column" key={index}>
                      <div
                        className="bar"
                        style={{ height: `${height}%` }}
                      ></div>
                    </div>
                  )
                )}
              </div>

              <div className="chart-labels">
                <span>Mar</span>
                <span>Apr</span>
                <span>May</span>
                <span>Jun</span>
                <span>Jul</span>
                <span>Aug</span>
              </div>
            </div>
          </div>
        </div>

        <div className="panel">
          <div className="panel-header">
            <div>
              <span className="panel-label">TALENT</span>
              <h3>Top performers</h3>
            </div>

            <button className="text-button">View all</button>
          </div>

          <div className="performers">
            <Person
              initials="AM"
              name="Alex Morgan"
              role="Software Engineer"
              score="96%"
            />

            <Person
              initials="SK"
              name="Sarah Kim"
              role="Data Analyst"
              score="93%"
            />

            <Person
              initials="DO"
              name="Daniel Okafor"
              role="AI Engineer"
              score="91%"
            />

            <Person
              initials="LN"
              name="Linda Nelson"
              role="Product Designer"
              score="89%"
            />
          </div>
        </div>
      </section>

      <section className="panel courses-panel">
        <div className="panel-header">
          <div>
            <span className="panel-label">
              LEARNING CENTER
            </span>

            <h3>Continue learning</h3>
          </div>

          <button className="text-button">
            Browse all courses →
          </button>
        </div>

        <div className="course-grid">
          <CourseCard
            title="Python for AI"
            category="Artificial Intelligence"
            progress={72}
            level="Intermediate"
          />

          <CourseCard
            title="Computer Vision"
            category="AI & Robotics"
            progress={48}
            level="Intermediate"
          />

          <CourseCard
            title="Machine Learning Fundamentals"
            category="Machine Learning"
            progress={31}
            level="Beginner"
          />
        </div>
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <span className="panel-label">
              TALENT LIFECYCLE
            </span>

            <h3>From hiring to high performance</h3>
          </div>
        </div>

        <div className="lifecycle">
          <Lifecycle
            number="01"
            title="Recruit"
            text="Evaluate candidates with structured assessments."
          />

          <div className="flow-arrow">→</div>

          <Lifecycle
            number="02"
            title="Evaluate"
            text="Measure technical and behavioral skills."
          />

          <div className="flow-arrow">→</div>

          <Lifecycle
            number="03"
            title="Onboard"
            text="Create personalized employee learning paths."
          />

          <div className="flow-arrow">→</div>

          <Lifecycle
            number="04"
            title="Develop"
            text="Track skills and continuously improve performance."
          />
        </div>
      </section>
    </div>
  );
}

/* =========================================================
   COURSES PAGE
========================================================= */

function CoursesPage() {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadCourses() {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(
          `${API_BASE_URL}/api/courses/`
        );

        if (!response.ok) {
          throw new Error(
            `Server returned ${response.status}`
          );
        }

        const data = await response.json();

        setCourses(data.courses || []);
      } catch (err) {
        console.error("Course loading error:", err);

        setError(
          "Unable to load courses from the AI Tutor server."
        );
      } finally {
        setLoading(false);
      }
    }

    loadCourses();
  }, []);

  return (
    <div className="content">
      {/* HEADER */}
      <section className="page-intro">
        <div>
          <span className="panel-label">
            LEARNING CENTER
          </span>

          <h3>Courses</h3>

          <p>
            Explore courses available across the AI Tutor
            learning platform.
          </p>
        </div>

        <button
          className="primary-button"
          onClick={() => window.location.reload()}
        >
          Refresh courses
        </button>
      </section>

      {/* COURSE SUMMARY */}
      <section className="metrics">
        <Metric
          label="Total courses"
          value={loading ? "—" : courses.length}
          change="Live"
          icon="▣"
        />

        <Metric
          label="Categories"
          value={
            loading
              ? "—"
              : new Set(
                  courses.map((course) => course.category)
                ).size
          }
          change="Live"
          icon="◉"
        />

        <Metric
          label="Beginner courses"
          value={
            loading
              ? "—"
              : courses.filter(
                  (course) => course.level === "Beginner"
                ).length
          }
          change="Live"
          icon="01"
        />

        <Metric
          label="Advanced courses"
          value={
            loading
              ? "—"
              : courses.filter(
                  (course) => course.level === "Advanced"
                ).length
          }
          change="Live"
          icon="AI"
        />
      </section>

      {/* LOADING */}
      {loading && (
        <section className="panel">
          <div className="empty-state">
            <div className="empty-icon">AI</div>

            <h3>Loading courses...</h3>

            <p>
              Connecting to the AI Tutor course database.
            </p>
          </div>
        </section>
      )}

      {/* ERROR */}
      {!loading && error && (
        <section className="panel">
          <div className="empty-state">
            <div className="empty-icon">!</div>

            <h3>Connection problem</h3>

            <p>{error}</p>
          </div>
        </section>
      )}

      {/* COURSES */}
      {!loading && !error && courses.length > 0 && (
        <section className="panel">
          <div className="panel-header">
            <div>
              <span className="panel-label">
                COURSE LIBRARY
              </span>

              <h3>
                {courses.length} courses available
              </h3>
            </div>
          </div>

          <div className="course-grid">
            {courses.map((course) => (
              <RealCourseCard
                key={course.id}
                course={course}
              />
            ))}
          </div>
        </section>
      )}

      {/* EMPTY */}
      {!loading && !error && courses.length === 0 && (
        <section className="panel">
          <div className="empty-state">
            <div className="empty-icon">AI</div>

            <h3>No courses found</h3>

            <p>
              The database currently contains no courses.
            </p>
          </div>
        </section>
      )}
    </div>
  );
}

/* =========================================================
   REAL COURSE CARD
========================================================= */

function RealCourseCard({ course }) {
  return (
    <div className="course-card">
      <div className="course-icon">
        AI
      </div>

      <span className="course-category">
        {course.category}
      </span>

      <h4>{course.title}</h4>

      <p>
        {course.description}
      </p>

      <div className="course-meta">
        <span>{course.level}</span>

        <strong>
          {course.duration}
        </strong>
      </div>

      <button className="course-button">
        View course →
      </button>
    </div>
  );
}

/* =========================================================
   EMPLOYEES PAGE
========================================================= */

function EmployeesPage() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadEmployees() {
      try {
        setLoading(true);
        setError("");

        const response = await fetch(
          `${API_BASE_URL}/api/employees/`
        );

        if (!response.ok) {
          throw new Error(
            `Server returned ${response.status}`
          );
        }

        const data = await response.json();

        setEmployees(data.employees || []);
      } catch (err) {
        console.error(
          "Employee loading error:",
          err
        );

        setError(
          "Unable to load employees from the AI Tutor server."
        );
      } finally {
        setLoading(false);
      }
    }

    loadEmployees();
  }, []);

  return (
    <div className="content">
      <section className="page-intro">
        <div>
          <span className="panel-label">
            PEOPLE MANAGEMENT
          </span>

          <h3>Employee Development</h3>

          <p>
            Manage employees, monitor learning progress,
            evaluate skills, and build personalized
            development paths.
          </p>
        </div>

        <button className="primary-button">
          + Add employee
        </button>
      </section>

      <section className="metrics">
        <Metric
          label="Total employees"
          value={
            loading ? "—" : employees.length
          }
          change="Live"
          icon="♙"
        />

        <Metric
          label="Active learners"
          value={
            loading ? "—" : employees.length
          }
          change="Live"
          icon="✓"
        />

        <Metric
          label="Average skill score"
          value="—"
          change="Coming next"
          icon="↗"
        />

        <Metric
          label="Learning completion"
          value="—"
          change="Coming next"
          icon="▣"
        />
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <span className="panel-label">
              EMPLOYEE DIRECTORY
            </span>

            <h3>Employees</h3>
          </div>

          <button
            className="small-button"
            onClick={() => window.location.reload()}
          >
            Refresh
          </button>
        </div>

        {loading && (
          <div className="empty-state">
            <div className="empty-icon">
              AI
            </div>

            <h3>Loading employees...</h3>

            <p>
              Connecting to the AI Tutor backend.
            </p>
          </div>
        )}

        {!loading && error && (
          <div className="empty-state">
            <div className="empty-icon">
              !
            </div>

            <h3>Connection problem</h3>

            <p>{error}</p>
          </div>
        )}

        {!loading &&
          !error &&
          employees.length === 0 && (
            <div className="empty-state">
              <div className="empty-icon">
                AI
              </div>

              <h3>No employees yet</h3>

              <p>
                Employees added to the organization
                will appear here.
              </p>
            </div>
          )}

        {!loading &&
          !error &&
          employees.length > 0 && (
            <div className="employee-table-wrapper">
              <table className="employee-table">
                <thead>
                  <tr>
                    <th>Employee</th>
                    <th>Email</th>
                    <th>ID</th>
                    <th>Status</th>
                    <th>Action</th>
                  </tr>
                </thead>

                <tbody>
                  {employees.map((employee) => (
                    <tr key={employee.id}>
                      <td>
                        <div className="employee-person">
                          <div className="person-avatar">
                            {getInitials(
                              employee.name
                            )}
                          </div>

                          <div>
                            <strong>
                              {employee.name}
                            </strong>

                            <span>
                              Employee
                            </span>
                          </div>
                        </div>
                      </td>

                      <td>
                        {employee.email}
                      </td>

                      <td>
                        #{employee.id}
                      </td>

                      <td>
                        <span className="status-active">
                          ● Active
                        </span>
                      </td>

                      <td>
                        <button className="table-action">
                          View profile →
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
      </section>

      <section className="panel">
        <div className="panel-header">
          <div>
            <span className="panel-label">
              NEXT DEVELOPMENT LAYER
            </span>

            <h3>Employee intelligence</h3>
          </div>
        </div>

        <div className="lifecycle">
          <Lifecycle
            number="01"
            title="Profile"
            text="Employee role, department, skills and background."
          />

          <div className="flow-arrow">→</div>

          <Lifecycle
            number="02"
            title="Assess"
            text="Measure technical and behavioral competency."
          />

          <div className="flow-arrow">→</div>

          <Lifecycle
            number="03"
            title="Learn"
            text="Assign courses based on skill gaps and goals."
          />

          <div className="flow-arrow">→</div>

          <Lifecycle
            number="04"
            title="Improve"
            text="Track development and performance over time."
          />
        </div>
      </section>
    </div>
  );
}

/* =========================================================
   HELPERS
========================================================= */

function getInitials(name = "") {
  return name
    .split(" ")
    .filter(Boolean)
    .slice(0, 2)
    .map((part) => part[0])
    .join("")
    .toUpperCase();
}

function Metric({
  label,
  value,
  change,
  icon,
}) {
  return (
    <div className="metric-card">
      <div className="metric-top">
        <span>{label}</span>

        <div className="metric-icon">
          {icon}
        </div>
      </div>

      <strong>{value}</strong>

      <div className="metric-change">
        <span>↗ {change}</span>

        <small>
          system data
        </small>
      </div>
    </div>
  );
}

function Person({
  initials,
  name,
  role,
  score,
}) {
  return (
    <div className="person">
      <div className="person-avatar">
        {initials}
      </div>

      <div className="person-info">
        <strong>{name}</strong>
        <span>{role}</span>
      </div>

      <div className="score">
        {score}
      </div>
    </div>
  );
}

function CourseCard({
  title,
  category,
  progress,
  level,
}) {
  return (
    <div className="course-card">
      <div className="course-icon">
        AI
      </div>

      <span className="course-category">
        {category}
      </span>

      <h4>{title}</h4>

      <div className="course-meta">
        <span>{level}</span>

        <strong>
          {progress}%
        </strong>
      </div>

      <div className="progress">
        <div
          style={{
            width: `${progress}%`,
          }}
        ></div>
      </div>

      <button className="course-button">
        Continue learning →
      </button>
    </div>
  );
}

function Lifecycle({
  number,
  title,
  text,
}) {
  return (
    <div className="lifecycle-item">
      <span>{number}</span>

      <h4>{title}</h4>

      <p>{text}</p>
    </div>
  );
}

function PlaceholderPage({
  title,
}) {
  return (
    <div className="content">
      <div className="empty-state">
        <div className="empty-icon">
          AI
        </div>

        <span className="panel-label">
          AI TUTOR 2.0
        </span>

        <h3>{title}</h3>

        <p>
          This module is part of the
          AI Tutor 2.0 enterprise platform.
          We will connect it to the backend
          next.
        </p>

        <button className="primary-button">
          Module coming next →
        </button>
      </div>
    </div>
  );
}

function getPageTitle(page) {
  const titles = {
    dashboard: "Executive Dashboard",
    courses: "Learning Center",
    assessments: "Assessments",
    employees: "Employee Development",
    candidates: "Candidate Evaluation",
    analytics: "Talent Analytics",
  };

  return (
    titles[page] ||
    "AI Tutor 2.0"
  );
}

export default App;