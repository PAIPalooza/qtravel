# **Semantic Seed Coding Standards: AI Travel Planner Edition**

## **Introduction**
These coding standards are tailored specifically for the AI Travel Planner project, ensuring our team builds a secure, high-quality travel planning application following XP-oriented development principles. This document adapts our global standards to the unique requirements of this project.

---

## **📋 Backlog Management for AI Travel Planner**

### **Project-Specific Workflow**
1. **Start the top unstarted story in the QTravel backlog**  
2. **Branch Naming Convention**:  
   - `feature/travel-{id}` for new features (e.g., `feature/travel-32-itinerary-generator`)  
   - `bug/travel-{id}` for bug fixes
   - `chore/travel-{id}` for maintenance tasks
3. **QTravel TDD Workflow**:  
   - Write failing tests for travel planning features (**WIP: Red Tests**)
   - Implement code for AI integration, trip planning, etc. (**WIP: Green Tests**)
   - Refactor and commit (**Refactor complete**)
4. **QTravel Pull Request Process**:  
   - Ensure all tests are passing, including AI interaction tests
   - Mark story **Finished**, create a **PR** with relevant screenshots
   - Merge only after review by at least one team member

---

## **📖 QTravel Story Estimation**

### **Project-Specific Estimation Guidelines**
- **1️⃣ Point**: Simple UI components, basic endpoint additions
- **2️⃣ Points**: New travel planner features with clear requirements
- **3️⃣ Points**: Complex UI interactions, AI prompt engineering
- **5️⃣ Points**: Integrations with third-party APIs (maps, booking)
- **8️⃣ Points**: Core AI functionality, complex personalization features

---

## **🎨 Coding Style Guidelines for AI Travel Planner**

### **Frontend Standards**
- **Component Structure**: React/Next.js components follow atomic design principles
- **Naming**: Use descriptive names (e.g., `TripPlannerForm.jsx`, `ItineraryDayView.jsx`)
- **Styling**: Use Tailwind CSS with consistent class ordering
- **State Management**: Prefer React Context for global state

### **Backend Standards**
- **API Structure**: REST principles, with versioned endpoints
- **Naming**: 
  - FastAPI: Use snake_case for functions and variables
  - Supabase: Table and column naming follows the schema in `datamodel.md`
- **Authentication**: Implement Supabase Auth with proper role-based permissions

### **AI Integration Standards**
- **Prompt Engineering**: Document all prompt templates in code comments
- **AI Class Structure**: Implement AI service classes with clear responsibility boundaries
- **Error Handling**: Always include fallback options for AI service failures

---

## **🧪 Testing Strategy for AI Travel Planner**

### **Project-Specific Testing**
1. **Unit Tests** 
   - Frontend: React Testing Library for component tests
   - Backend: Pytest for API endpoints and services
   - AI: Mock responses for deterministic testing

2. **BDD-Style Integration Tests**
```javascript
describe('Itinerary Generator', () => {
  describe('personalization', () => {
    it('should consider user preferences when generating itineraries', () => {
      const mockUser = createUserWithPreferences(['food', 'culture']);
      const itinerary = generateItinerary(mockUser, 'Tokyo', 5);
      expect(itinerary.items.some(i => i.type === 'food')).to.be.true;
    });
  });
});
```

3. **AI-Specific Testing**
   - Snapshot tests for AI response formatting
   - Regression tests for prompt engineering changes
   - Performance tests for response time requirements

---

## **🔄 CI/CD Pipeline for AI Travel Planner**

### **Project-Specific Pipeline**
- **Linting**: ESLint (frontend), Flake8/Black (backend)
- **Testing**: Jest (frontend), Pytest (backend)
- **Staging**: Deploy to Vercel Preview environments
- **Production**: Automated deployment after PR approval

---

## **🔧 Version Control Practices**

### **QTravel-Specific Guidelines**
- **PR Size**: Limit to 400 lines of changes where possible
- **Feature Branches**: Always branch from `main` for new features
- **Commit Messages**: Prefix with feature area:
  - `[UI]` for frontend changes
  - `[API]` for backend changes 
  - `[AI]` for AI-related code
  - `[DB]` for database schema changes
- **WIP Commits**: Daily commits even for incomplete work

---

## **🔒 Security Standards for Travel Data**

### **Travel-Specific Security Guidelines**
- **User Data**: No PII stored outside of Supabase
- **API Keys**: All external service credentials in environment variables
- **Trip Data**: Implement proper access controls for shared trips
- **AI Interaction Logs**: Sanitize and anonymize before storage

---

## **🧠 AI Engineering Standards**

### **QTravel AI Implementation Guidelines**
- **Prompt Templates**: Store in version-controlled templates
- **AI Models**: Document version and parameters used
- **Error Handling**: Implement graceful fallbacks for AI failures
- **Telemetry**: Log AI interaction metrics for optimization

---

## **📱 UI/UX Guidelines**

### **QTravel-Specific Design Standards**
- **Color Palette**: Adhere to travel-themed palette in UI components
- **Accessibility**: WCAG AA compliance for all UI elements
- **Responsive Design**: Support desktop, tablet, and mobile layouts
- **Loading States**: Implement skeleton UI for AI-generated content

---

By following these project-specific coding standards, we'll build a high-quality AI Travel Planner that delivers excellent user experience while maintaining code quality, security, and development efficiency.
