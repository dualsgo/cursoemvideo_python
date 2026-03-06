import React, { useState, useEffect } from 'react';
import {
    Terminal,
    BookOpen,
    ChevronRight,
    ChevronDown,
    Code,
    Activity,
    Cpu,
    Award,
    Home,
    Settings,
    LogOut,
    Folder,
    FileCode,
    Search,
    Zap,
    ExternalLink
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import data from './data.json';
import Sandbox from './components/Sandbox';

const SidebarItem = ({ icon: Icon, label, active, onClick }) => (
    <button
        onClick={onClick}
        className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 ${active
            ? 'bg-blue-600/20 text-blue-400 border-r-4 border-blue-500'
            : 'hover:bg-white/5 text-gray-400'
            }`}
    >
        <Icon size={20} />
        <span className="font-medium">{label}</span>
    </button>
);

const FolderSection = ({ name, content, level = 0 }) => {
    const [isOpen, setIsOpen] = useState(level === 0 || level === 1);

    const folders = Object.keys(content).filter(key => key !== 'files');
    const files = content.files || [];

    if (folders.length === 0 && files.length === 0) return null;

    return (
        <div className="mb-2">
            <button
                onClick={() => setIsOpen(!isOpen)}
                className="w-full flex items-center gap-2 p-2 hover:bg-white/5 rounded-lg text-slate-300 transition-colors group"
            >
                <div className="text-gray-500">
                    {isOpen ? <ChevronDown size={16} /> : <ChevronRight size={16} />}
                </div>
                <Folder className={isOpen ? 'text-blue-400' : 'text-slate-500'} size={18} />
                <span className={`text-sm font-medium ${isOpen ? 'text-white' : ''}`}>{name}</span>
                <span className="ml-auto text-[10px] bg-slate-800 px-2 py-0.5 rounded-full text-slate-500 opacity-0 group-hover:opacity-100 transition-opacity">
                    {folders.length + files.length} itens
                </span>
            </button>

            <AnimatePresence>
                {isOpen && (
                    <motion.div
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: 'auto', opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        className="ml-6 border-l border-slate-800/50 pl-2 overflow-hidden"
                    >
                        {folders.map(folderName => (
                            <FolderSection
                                key={folderName}
                                name={folderName}
                                content={content[folderName]}
                                level={level + 1}
                            />
                        ))}
                        {files.map(fileName => (
                            <div
                                key={fileName}
                                className="flex items-center gap-2 p-2 hover:bg-blue-500/10 rounded-lg text-slate-400 hover:text-blue-300 cursor-pointer group transition-all"
                            >
                                <FileCode size={16} className="text-yellow-500/70" />
                                <span className="text-xs">{fileName}</span>
                                <Zap size={12} className="ml-auto opacity-0 group-hover:opacity-100 text-yellow-500" />
                            </div>
                        ))}
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
};

const DashboardHome = ({ stats, searchTerm, setSearchTerm, data }) => (
    <div className="max-w-6xl mx-auto relative z-10">
        {/* Header */}
        <header className="flex justify-between items-center mb-12">
            <div>
                <h2 className="text-3xl font-bold text-white mb-2">Bem-vindo de volta, Dev! 🚀</h2>
                <p className="text-slate-400">Continue sua jornada para se tornar um mestre em Python.</p>
            </div>

            <div className="relative group">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500 group-focus-within:text-blue-400 transition-colors" size={18} />
                <input
                    type="text"
                    placeholder="Pesquisar desafios..."
                    className="bg-slate-900/50 border border-slate-800 rounded-full py-2.5 pl-10 pr-6 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/30 w-72 transition-all"
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                />
            </div>
        </header>

        {/* Stats Grid */}
        <div className="grid grid-cols-4 gap-6 mb-12">
            {stats.map((stat, idx) => (
                <motion.div
                    key={idx}
                    whileHover={{ y: -5 }}
                    className="bg-slate-900/40 backdrop-blur-md border border-slate-800/60 p-6 rounded-2xl relative overflow-hidden group"
                >
                    <div className={`absolute top-0 right-0 p-3 opacity-10 group-hover:scale-110 transition-transform ${stat.color}`}>
                        <stat.icon size={48} />
                    </div>
                    <div className={`p-2 rounded-lg bg-slate-800 shadow-inner inline-block mb-4 ${stat.color}`}>
                        <stat.icon size={20} />
                    </div>
                    <div className="text-2xl font-bold text-white mb-1">{stat.value}</div>
                    <div className="text-sm text-slate-400 font-medium">{stat.label}</div>
                </motion.div>
            ))}
        </div>

        {/* Content Sections */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Explorer */}
            <div className="md:col-span-2">
                <div className="bg-[#0e0e11] rounded-3xl border border-slate-800 overflow-hidden shadow-2xl">
                    <div className="p-6 border-b border-slate-800 flex justify-between items-center bg-white/5">
                        <h3 className="font-semibold text-white flex items-center gap-2">
                            <Folder size={18} className="text-blue-400" />
                            Explorer do Curso
                        </h3>
                        <div className="flex gap-2">
                            <span className="w-3 h-3 rounded-full bg-red-500/50" />
                            <span className="w-3 h-3 rounded-full bg-yellow-500/50" />
                            <span className="w-3 h-3 rounded-full bg-green-500/50" />
                        </div>
                    </div>
                    <div className="p-6 h-[500px] overflow-y-auto custom-scrollbar">
                        {Object.keys(data).filter(key => key !== 'files').map(mundo => (
                            <FolderSection key={mundo} name={mundo} content={data[mundo]} />
                        ))}
                    </div>
                </div>
            </div>

            {/* Activities */}
            <div className="space-y-6">
                <div className="bg-slate-900/40 backdrop-blur-md border border-slate-800 p-6 rounded-3xl">
                    <h3 className="font-semibold text-white mb-6 flex items-center gap-2">
                        <Activity size={18} className="text-green-400" />
                        Atividade Recente
                    </h3>
                    <div className="space-y-4">
                        {[
                            { title: 'Desafio 115', time: 'Há 2 horas', status: 'completed' },
                            { title: 'Aula #023', time: 'Ontem', status: 'in-progress' },
                            { title: 'Desafio 114', time: 'Há 2 dias', status: 'completed' },
                        ].map((item, i) => (
                            <div key={i} className="flex items-center gap-4 bg-white/5 p-3 rounded-xl border border-white/5 hover:border-white/10 transition-colors cursor-pointer group hover:bg-white/10">
                                <div className={`w-2 h-2 rounded-full ${item.status === 'completed' ? 'bg-green-500' : 'bg-yellow-500 shadow-lg shadow-yellow-500/40'}`} />
                                <div className="flex-1">
                                    <div className="text-sm font-medium text-slate-200">{item.title}</div>
                                    <div className="text-[10px] text-slate-500 uppercase tracking-wider">{item.time}</div>
                                </div>
                                <ExternalLink size={14} className="text-slate-600 opacity-0 group-hover:opacity-100 transition-opacity" />
                            </div>
                        ))}
                    </div>
                </div>

                <div className="bg-gradient-to-br from-blue-600/20 to-indigo-600/20 border border-blue-500/30 p-8 rounded-3xl relative overflow-hidden group cursor-pointer shadow-xl shadow-blue-500/10">
                    <div className="absolute -right-4 -bottom-4 opacity-10 group-hover:scale-110 group-hover:-rotate-12 transition-all duration-500">
                        <Cpu size={120} />
                    </div>
                    <h3 className="text-xl font-bold text-white mb-2">Novo Desafio!</h3>
                    <p className="text-sm text-blue-200/80 mb-6">Módulo de POO desbloqueado. Comece agora.</p>
                    <motion.button
                        whileTap={{ scale: 0.95 }}
                        className="bg-white text-blue-600 px-6 py-2.5 rounded-2xl text-sm font-bold shadow-lg shadow-white/10 hover:shadow-white/30 transition-all flex items-center gap-2"
                    >
                        Continuar
                        <ChevronRight size={16} />
                    </motion.button>
                </div>
            </div>
        </div>
    </div>
);

function App() {
    const [activeTab, setActiveTab] = useState('Home');
    const [searchTerm, setSearchTerm] = useState('');

    const stats = [
        { label: 'Mundos', value: '4', icon: Home, color: 'text-blue-500' },
        { label: 'Exercícios', value: '115+', icon: Code, color: 'text-yellow-500' },
        { label: 'Aulas', value: '30+', icon: BookOpen, color: 'text-green-500' },
        { label: 'Conclusão', value: '78%', icon: Award, color: 'text-purple-500' },
    ];

    return (
        <div className="flex h-screen bg-[#0a0a0c] overflow-hidden">
            {/* Sidebar */}
            <div className="w-64 border-r border-slate-800 bg-[#0e0e11] p-6 flex flex-col gap-6">
                <div className="flex items-center gap-3 px-2 mb-4">
                    <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-xl flex items-center justify-center shadow-lg shadow-blue-500/20">
                        <Terminal className="text-white" size={24} />
                    </div>
                    <h1 className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-400">
                        Python Academy
                    </h1>
                </div>

                <nav className="flex-1 flex flex-col gap-2">
                    <SidebarItem icon={Home} label="Dashboard" active={activeTab === 'Home'} onClick={() => setActiveTab('Home')} />
                    <SidebarItem icon={Code} label="Sandbox Editor" active={activeTab === 'Sandbox'} onClick={() => setActiveTab('Sandbox')} />
                    <SidebarItem icon={BookOpen} label="Conteúdo" active={activeTab === 'Conteudo'} onClick={() => setActiveTab('Conteudo')} />
                    <SidebarItem icon={Activity} label="Estatísticas" active={activeTab === 'Stats'} onClick={() => setActiveTab('Stats')} />
                    <div className="mt-auto pt-6 border-t border-slate-800">
                        <SidebarItem icon={Settings} label="Configurações" onClick={() => { }} />
                        <SidebarItem icon={LogOut} label="Sair" onClick={() => { }} />
                    </div>
                </nav>
            </div>

            {/* Main Content */}
            <main className="flex-1 overflow-y-auto p-10 relative">
                {/* Background glow */}
                <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-blue-600/5 blur-[120px] rounded-full pointer-events-none" />
                <div className="absolute bottom-0 left-0 w-[300px] h-[300px] bg-purple-600/5 blur-[100px] rounded-full pointer-events-none" />

                {activeTab === 'Home' && (
                    <DashboardHome
                        stats={stats}
                        searchTerm={searchTerm}
                        setSearchTerm={setSearchTerm}
                        data={data}
                    />
                )}

                {activeTab === 'Sandbox' && (
                    <div className="max-w-6xl mx-auto h-full flex flex-col">
                        <header className="mb-8">
                            <h2 className="text-3xl font-bold text-white mb-2">Python Sandbox Editor</h2>
                            <p className="text-slate-400">Experimente snippets, teste lógicas e pratiquem seus exercícios sem sair do dashboard.</p>
                        </header>
                        <div className="flex-1 min-h-0">
                            <Sandbox />
                        </div>
                    </div>
                )}

                {(activeTab === 'Conteudo' || activeTab === 'Stats') && (
                    <div className="max-w-6xl mx-auto flex flex-col items-center justify-center h-[70%] text-center opacity-70">
                        <div className="p-6 bg-slate-900/50 rounded-full mb-6 border border-slate-800">
                            <Zap size={48} className="text-blue-500 animate-pulse" />
                        </div>
                        <h2 className="text-2xl font-bold text-white mb-2">Módulo em Desenvolvimento</h2>
                        <p className="text-slate-400">Estamos trabalhando para trazer a melhor experiência de {activeTab.toLowerCase()}.</p>
                        <button
                            onClick={() => setActiveTab('Home')}
                            className="mt-6 text-blue-400 hover:text-blue-300 font-medium transition-colors"
                        >
                            Voltar para o Dashboard
                        </button>
                    </div>
                )}
            </main>
        </div>
    );
}

export default App;

