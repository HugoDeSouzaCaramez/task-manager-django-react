import React, { useEffect, useState } from 'react';
import { Task } from './api/tasks';
import { fetchTasks } from './api/tasks';

const TaskList: React.FC = () => {
    const [tasks, setTasks] = useState<Task[]>([]);

    useEffect(() => {
        const loadTasks = async () => {
            const data = await fetchTasks();
            setTasks(data);
        };
        loadTasks();
    }, []);

    return (
        <div>
            {tasks.length === 0 ? (
                <p>Nenhuma tarefa encontrada.</p>
            ) : (
                tasks.map(task => (
                    <div key={task.id}>
                        <h3>{task.title}</h3>
                        <p>{task.description}</p>
                    </div>
                ))
            )}
        </div>
    );
};

export default TaskList;