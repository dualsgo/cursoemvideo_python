import React, { useState } from 'react';
import { Play, Terminal, Code, Cpu, Sparkles, X, Copy, Check } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const Sandbox = ({ initialCode = "# Digite seu código Python aqui...\nprint('Olá Mundo Python!')" }) => {
    const [code, setCode] = useState(initialCode);
    const [output, setOutput] = useState([]);
    const [isRunning, setIsRunning] = useState(false);
    const [copied, setCopied] = useState(false);

    const runCode = () => {
        setIsRunning(true);
        setOutput([{ type: 'info', content: 'Iniciando execução no ambiente seguro...' }]);

        // Simulação de execução (Mock)
        // Para um ambiente real, precisaríamos do Pyodide ou backend
        setTimeout(() => {
            try {
                // Mock de processamento de output baseado no código
                let mockOutput = [];
                if (code.includes('print')) {
                    const match = code.match(/print\(['"](.+)['"]\)/);
                    mockOutput.push({ type: 'stdout', content: match ? match[1] : 'Saída do programa...' });
                } else {
                    mockOutput.push({ type: 'stdout', content: '>>> Código executado com sucesso (sem output).' });
                }

                setOutput(prev => [...prev, ...mockOutput]);
            } catch (err) {
                setOutput(prev => [...prev, { type: 'error', content: 'Erro de Sintaxe: Verifique seu código.' }]);
            }
            setIsRunning(false);
        }, 1200);
    };

    const copyCode = () => {
        navigator.clipboard.writeText(code);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <div className="flex flex-col gap-6 h-full">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 flex-1">
                {/* Editor Container */}
                <div className="flex flex-col bg-[#0e0e11] rounded-3xl border border-slate-800 overflow-hidden shadow-2xl">
                    <div className="p-4 border-b border-slate-800 flex justify-between items-center bg-white/5">
                        <div className="flex items-center gap-2">
                            <div className="flex gap-1.5 mr-2">
                                <span className="w-3 h-3 rounded-full bg-red-500/50" />
                                <span className="w-3 h-3 rounded-full bg-yellow-500/50" />
                                <span className="w-3 h-3 rounded-full bg-green-500/50" />
                            </div>
                            <Code size={16} className="text-blue-400" />
                            <span className="text-sm font-semibold text-slate-300">main.py</span>
                        </div>
                        <div className="flex gap-2">
                            <button
                                onClick={copyCode}
                                className="p-2 hover:bg-white/10 rounded-lg text-slate-400 transition-colors"
                                title="Copiar Código"
                            >
                                {copied ? <Check size={16} className="text-green-500" /> : <Copy size={16} />}
                            </button>
                            <button
                                onClick={runCode}
                                disabled={isRunning}
                                className={`flex items-center gap-2 px-4 py-1.5 rounded-xl text-sm font-bold transition-all ${isRunning
                                        ? 'bg-slate-800 text-slate-500'
                                        : 'bg-blue-600 hover:bg-blue-500 text-white shadow-lg shadow-blue-600/20'
                                    }`}
                            >
                                {isRunning ? <Sparkles size={16} className="animate-spin" /> : <Play size={16} fill="currentColor" />}
                                {isRunning ? 'Executando...' : 'Rodar'}
                            </button>
                        </div>
                    </div>

                    <div className="relative flex-1 group">
                        <textarea
                            value={code}
                            onChange={(e) => setCode(e.target.value)}
                            className="w-full h-full bg-transparent p-6 text-blue-100/90 font-mono text-sm focus:outline-none resize-none custom-scrollbar leading-relaxed"
                            spellCheck="false"
                        />
                        <div className="absolute right-4 bottom-4 opacity-10 pointer-events-none group-focus-within:opacity-20 transition-opacity font-bold italic text-4xl">
                            Python 3.x
                        </div>
                    </div>
                </div>

                {/* Terminal Container */}
                <div className="flex flex-col bg-slate-950 rounded-3xl border border-slate-800 overflow-hidden shadow-2xl">
                    <div className="p-4 border-b border-slate-800 flex justify-between items-center bg-black/40">
                        <div className="flex items-center gap-2">
                            <Terminal size={16} className="text-green-400" />
                            <span className="text-sm font-semibold text-slate-300">Console de Saída</span>
                        </div>
                        <button
                            onClick={() => setOutput([])}
                            className="text-xs text-slate-500 hover:text-slate-300 transition-colors flex items-center gap-1"
                        >
                            <X size={12} /> Limpar
                        </button>
                    </div>

                    <div className="flex-1 p-6 font-mono text-sm overflow-y-auto custom-scrollbar bg-black/20">
                        {output.length === 0 ? (
                            <div className="flex flex-col items-center justify-center h-full text-slate-600 opacity-50">
                                <Cpu size={48} className="mb-4" />
                                <p>Aguardando execução...</p>
                            </div>
                        ) : (
                            <div className="space-y-2">
                                {output.map((line, i) => (
                                    <motion.div
                                        initial={{ opacity: 0, x: -10 }}
                                        animate={{ opacity: 1, x: 0 }}
                                        key={i}
                                        className={`flex gap-3 ${line.type === 'error' ? 'text-red-400' :
                                                line.type === 'info' ? 'text-blue-400 italic opacity-70' :
                                                    'text-green-400'
                                            }`}
                                    >
                                        <span className="shrink-0 text-slate-700">{line.type === 'stdout' ? '>>>' : '::'}</span>
                                        <span className="break-all">{line.content}</span>
                                    </motion.div>
                                ))}
                                {isRunning && (
                                    <div className="flex gap-3 text-slate-600 animate-pulse">
                                        <span className="shrink-0 text-slate-800">>>></span>
                                        <span>_</span>
                                    </div>
                                )}
                            </div>
                        )}
                    </div>
                </div>
            </div>

            {/* Footer Info */}
            <div className="bg-blue-600/5 border border-blue-500/10 p-4 rounded-2xl flex items-center gap-4">
                <div className="p-2 bg-blue-500/10 rounded-lg text-blue-400">
                    <Sparkles size={18} />
                </div>
                <p className="text-xs text-slate-400 leading-relaxed">
                    <strong className="text-blue-300">Dica:</strong> Para rodar nativamente com <code className="bg-slate-800 px-1.5 py-0.5 rounded text-blue-200">print()</code> e entradas,
                    estamos integrando o motor do Python diretamente no seu navegador em breve.
                </p>
            </div>
        </div>
    );
};

export default Sandbox;
