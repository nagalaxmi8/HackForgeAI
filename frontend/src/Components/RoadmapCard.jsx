import {
    CalendarDays,
    FolderOpen,
    Code2,
    Cpu,
    Bug,
    Rocket,
    Sparkles,
    Target,
  } from "lucide-react";
  
  function RoadmapCard({ data }) {
    if (!data) return null;
  
    const getTaskIcon = (title = "") => {
      const text = title.toLowerCase();
  
      if (text.includes("setup")) return <FolderOpen size={22} />;
      if (text.includes("frontend")) return <Code2 size={22} />;
      if (text.includes("backend")) return <Cpu size={22} />;
      if (text.includes("testing")) return <Bug size={22} />;
      if (text.includes("deploy")) return <Rocket size={22} />;
  
      return <Sparkles size={22} />;
    };
  
    const subtitles = [
      "Foundation & Setup",
      "Development",
      "Polish & Deploy",
    ];
  
    const goals = [
      "Build Foundation",
      "Core Features",
      "Ready for Demo",
    ];
  
    return (
      <div className="card roadmap-wrapper">
  
        <div className="roadmap-top">
  
          <div>
  
            <h2 className="card-title">
              📅 Development Roadmap
            </h2>
  
  
          </div>
  
          <div className="roadmap-pill">
            🚀 {Object.keys(data).length}-Day Plan
          </div>
  
        </div>
  
        <div className="roadmap-grid">
        {Object.entries(data).map(([day, dayData]) => (

<div className="day-card" key={day}>

  <div className="day-header">

    <div className="day-icon">
      <CalendarDays size={28} />
    </div>

    <div>
      <h3>{day.replace("_", " ").toUpperCase()}</h3>
      <span>{dayData.subtitle}</span>
    </div>

  </div>

  <div className="mini-tasks">

    {dayData.tasks?.slice(0, 3).map((task, index) => (

      <div className="mini-task" key={index}>

        <div className="mini-icon">
          {getTaskIcon(task.title)}
        </div>

        <div>
          <h4>{task.title}</h4>
          <p>{task.description}</p>
        </div>

      </div>

    ))}

  </div>

  <div className="goal-box">

    <Target size={18} />

    <strong>Goal:</strong>

    <span>{dayData.goal}</span>

  </div>

</div>

))}
          
  
        </div>
  
      </div>
    );
  }
  
  export default RoadmapCard;