import { render, screen, waitFor } from '@testing-library/react';
import TaskList from './TaskList';
import { Task } from './api/tasks';
import { fetchTasks } from './api/tasks';
//import '@testing-library/jest-dom/extend-expect';
import '@testing-library/jest-dom';

// Mock da função fetchTasks
jest.mock('./api/tasks', () => ({
  fetchTasks: jest.fn(),
}));

const mockTasks: Task[] = [
  {
    id: 1,
    title: 'Tarefa Teste 1',
    description: 'Descrição da Tarefa 1',
    is_completed: false,
  },
  {
    id: 2,
    title: 'Tarefa Teste 2',
    description: 'Descrição da Tarefa 2',
    is_completed: true,
  },
];

describe('TaskList Component', () => {
  beforeEach(() => {
    // Resetar o mock antes de cada teste
    (fetchTasks as jest.Mock).mockClear();
  });

  it('deve exibir uma lista de tarefas após carregar os dados', async () => {
    // Configurar o mock para retornar dados falsos
    (fetchTasks as jest.Mock).mockResolvedValue(mockTasks);

    render(<TaskList />);

    // Aguardar o carregamento dos dados
    await waitFor(() => {
      expect(screen.getByText('Tarefa Teste 1')).toBeInTheDocument();
      expect(screen.getByText('Descrição da Tarefa 2')).toBeInTheDocument();
    });
  });

  it('deve chamar a API fetchTasks uma vez ao montar o componente', async () => {
    (fetchTasks as jest.Mock).mockResolvedValue([]);

    render(<TaskList />);

    await waitFor(() => {
      expect(fetchTasks).toHaveBeenCalledTimes(1);
    });
  });

  it('deve exibir mensagem se não houver tarefas', async () => {
    (fetchTasks as jest.Mock).mockResolvedValue([]);

    render(<TaskList />);

    await waitFor(() => {
      expect(screen.getByText('Nenhuma tarefa encontrada.')).toBeInTheDocument();
    });
  });
});