import { useState } from "react";
import axios from "../Services/api";

import Loading from "../Components/Loading";
import FeasibilityCard from "../Components/FeasibilityCard";
import ArchitectureCard from "../Components/ArchitectureCard";
import TaskCard from "../Components/TaskCard";
import RoadmapCard from "../Components/RoadmapCard";
import dummyData from "../Data/dummyData";
import {
    Sparkles,
    Brain,
    Users,
    CalendarDays,
    Wand2
  } from "lucide-react";
function Home() {
  const [projectIdea, setProjectIdea] = useState("");
  const [teamSize, setTeamSize] = useState(3);
  const [skills, setSkills] = useState("");
  const [deadline, setDeadline] = useState(3);

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!projectIdea.trim()) {
      alert("Please enter a project idea.");
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      const response = await axios.post("/analyze", {
        project_idea: projectIdea,
        team_size: Number(teamSize),
        skills: skills
          .split(",")
          .map((s) => s.trim())
          .filter((s) => s !== ""),
        deadline_days: Number(deadline),
      });

      setResult(response.data.data);
    } catch (error) {
      console.error(error);
      alert("Failed to connect to backend.");
    }

    setLoading(false);
  };

  return (
    <div className="container">

<div className="hero">

<div className="hero-badge">
  <Sparkles size={16}/>
  AI Powered Hackathon Planner
</div>

<h1 className="hero-title">
  HackForge AI
</h1>

<h2 className="hero-subtitle">
  Plan. Build. Win Hackathons.
</h2>

<p className="hero-description">
  Generate complete software architecture, feasibility analysis,
  team task allocation and development roadmaps using AI agents —
  all within seconds.
</p>

<div className="hero-features">

  <div className="feature-pill">
    <Brain size={18}/>
    AI Architecture
  </div>

  <div className="feature-pill">
    <Users size={18}/>
    Team Tasks
  </div>

  <div className="feature-pill">
    <CalendarDays size={18}/>
    Smart Roadmaps
  </div>

</div>

</div>

      <div className="hero-card">

  <div className="hero-card-header">

    <h3>Describe Your Project</h3>

    <p>
      Tell HackForge AI about your hackathon idea and we'll generate a complete development plan.
    </p>

  </div>

  <div className="form-group">

    <label>Project Idea</label>

    <textarea
      rows="6"
      placeholder="Example: Build an AI-powered platform that analyzes hackathon ideas, generates architecture, assigns team tasks, and creates a development roadmap."
      value={projectIdea}
      onChange={(e) => setProjectIdea(e.target.value)}
    />

  </div>

  <div className="row">

    <div className="input-group">

      <label>Team Size</label>

      <input
        type="number"
        min="1"
        value={teamSize}
        onChange={(e) => setTeamSize(e.target.value)}
      />

    </div>

    <div className="input-group">

      <label>Deadline (Days)</label>

      <input
        type="number"
        min="1"
        value={deadline}
        onChange={(e) => setDeadline(e.target.value)}
      />

    </div>

  </div>

  <div className="form-group">

    <label>Skills</label>

    <input
      type="text"
      placeholder="React, Python, FastAPI, Gemini"
      value={skills}
      onChange={(e) => setSkills(e.target.value)}
    />

  </div>

  <button className="generate-btn" onClick={handleSubmit}>

    <Wand2 size={18}/>

    Generate AI Plan

</button>

</div>

      {loading && <Loading />}

      {result && (
        <>
          <FeasibilityCard data={result.feasibility} />

          <ArchitectureCard data={result.architecture} />

          <TaskCard data={result.tasks} />

          <RoadmapCard data={result.roadmap} />
        </>
      )}

    </div>
  );
}

export default Home;