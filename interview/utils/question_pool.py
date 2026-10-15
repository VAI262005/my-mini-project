import re
import random
from difflib import SequenceMatcher

# -----------------------------------------------------------------------------
# Comprehensive Job Role Question Pools
# Categorized by: job_role, difficulty, topic, question_type, keywords
# Formatted with natural conversational phrasing
# -----------------------------------------------------------------------------

JOB_ROLE_QUESTION_POOLS = {
    'Software Developer': [
        {
            'text': "Could you explain the core Object-Oriented Programming (OOP) concepts and how you have actually applied them in your code?",
            'difficulty': 'Medium',
            'topic': 'OOP',
            'question_type': 'Technical',
            'keywords': ['oop', 'object', 'class', 'inheritance', 'polymorphism', 'encapsulation', 'abstraction']
        },
        {
            'text': "I'd love to hear about a software project you developed recently. Could you walk me through what you built and your architecture design?",
            'difficulty': 'Medium',
            'topic': 'Projects',
            'question_type': 'Project',
            'keywords': ['project', 'built', 'developed', 'architecture', 'system', 'app', 'application']
        },
        {
            'text': "Suppose your application suddenly encounters a runtime error or produces incorrect output. How do you step through and debug the code?",
            'difficulty': 'Easy',
            'topic': 'Problem Solving',
            'question_type': 'Situational',
            'keywords': ['debug', 'error', 'bug', 'print', 'log', 'traceback', 'breakpoint', 'fix']
        },
        {
            'text': "Could you explain the structural and memory allocation differences between an array and a linked list?",
            'difficulty': 'Medium',
            'topic': 'DSA',
            'question_type': 'Technical',
            'keywords': ['array', 'linked list', 'list', 'memory', 'pointer', 'contiguous', 'node']
        },
        {
            'text': "If you noticed an algorithm in your codebase running with high time complexity like O(N^2), what steps would you take to optimize it?",
            'difficulty': 'Hard',
            'topic': 'DSA',
            'question_type': 'Problem Solving',
            'keywords': ['optimize', 'complexity', 'time complexity', 'space complexity', 'hash map', 'big o']
        },
        {
            'text': "How do you handle exceptions in your applications to ensure a smooth user experience even when unexpected errors occur?",
            'difficulty': 'Easy',
            'topic': 'Programming',
            'question_type': 'Technical',
            'keywords': ['exception', 'try', 'catch', 'except', 'error', 'throw', 'handling']
        },
        {
            'text': "Could you describe your experience with unit testing and automated continuous integration pipelines?",
            'difficulty': 'Medium',
            'topic': 'System Design',
            'question_type': 'Technical',
            'keywords': ['test', 'unit test', 'pytest', 'junit', 'ci/cd', 'integration', 'automation']
        }
    ],

    'Frontend Developer': [
        {
            'text': "Could you walk me through the primary responsibilities of HTML, CSS, and JavaScript in creating modern web applications?",
            'difficulty': 'Easy',
            'topic': 'Web Fundamentals',
            'question_type': 'Technical',
            'keywords': ['html', 'css', 'javascript', 'js', 'markup', 'style', 'script']
        },
        {
            'text': "What is the Document Object Model (DOM), and how do browsers handle DOM manipulation and re-rendering efficiently?",
            'difficulty': 'Medium',
            'topic': 'DOM',
            'question_type': 'Technical',
            'keywords': ['dom', 'document', 'node', 'element', 'event', 'listener', 'render']
        },
        {
            'text': "How do you go about implementing responsive layouts that look seamless across both mobile devices and desktop monitors?",
            'difficulty': 'Medium',
            'topic': 'CSS',
            'question_type': 'Technical',
            'keywords': ['responsive', 'media query', 'flexbox', 'grid', 'viewport', 'mobile']
        },
        {
            'text': "In React development, how do you decide whether data should live in component state versus being passed down via props?",
            'difficulty': 'Medium',
            'topic': 'Frontend Frameworks',
            'question_type': 'Technical',
            'keywords': ['react', 'state', 'props', 'component', 'hooks', 'usestate']
        },
        {
            'text': "When a web application takes too long to load, what frontend performance techniques do you apply to speed it up?",
            'difficulty': 'Hard',
            'topic': 'Optimization',
            'question_type': 'Problem Solving',
            'keywords': ['performance', 'bundle', 'lazy loading', 'cache', 'minification', 'assets', 'cdn']
        },
        {
            'text': "Could you explain how asynchronous JavaScript works, specifically Promises and the async/await pattern?",
            'difficulty': 'Medium',
            'topic': 'Programming',
            'question_type': 'Technical',
            'keywords': ['async', 'await', 'promise', 'fetch', 'api', 'callback', 'event loop']
        }
    ],

    'Backend Developer': [
        {
            'text': "Could you explain RESTful API design principles and the HTTP methods you commonly use when designing backend endpoints?",
            'difficulty': 'Medium',
            'topic': 'API',
            'question_type': 'Technical',
            'keywords': ['rest', 'api', 'http', 'get', 'post', 'put', 'delete', 'endpoint']
        },
        {
            'text': "How do you approach designing database schemas to prevent data redundancy while maintaining relational integrity?",
            'difficulty': 'Medium',
            'topic': 'Database',
            'question_type': 'System Design',
            'keywords': ['database', 'schema', 'normalization', 'primary key', 'foreign key', 'relational']
        },
        {
            'text': "What security mechanisms, like JWT or OAuth, do you implement to safeguard your backend services from unauthorized access?",
            'difficulty': 'Hard',
            'topic': 'Security',
            'question_type': 'Technical',
            'keywords': ['jwt', 'oauth', 'token', 'auth', 'session', 'cookie', 'password', 'hash']
        },
        {
            'text': "If your backend server suddenly experiences a surge in concurrent traffic, how would you design the architecture to scale under heavy load?",
            'difficulty': 'Hard',
            'topic': 'System Design',
            'question_type': 'Situational',
            'keywords': ['scale', 'load balancer', 'redis', 'cache', 'queue', 'concurrency', 'worker']
        },
        {
            'text': "What is middleware in backend web frameworks, and how have you used it for request processing or authentication?",
            'difficulty': 'Medium',
            'topic': 'Frameworks',
            'question_type': 'Technical',
            'keywords': ['middleware', 'django', 'express', 'node', 'request', 'response', 'pipeline']
        }
    ],

    'Full Stack Developer': [
        {
            'text': "Could you describe the full lifecycle of an application request, from when a user clicks in the browser to the backend database query and back?",
            'difficulty': 'Medium',
            'topic': 'Full Stack',
            'question_type': 'Technical',
            'keywords': ['full stack', 'browser', 'dns', 'http', 'controller', 'database', 'json']
        },
        {
            'text': "How do you handle state synchronization between client-side components and server-side database tables?",
            'difficulty': 'Hard',
            'topic': 'Architecture',
            'question_type': 'Problem Solving',
            'keywords': ['state', 'react', 'redux', 'api', 'cache', 'sync', 'crud']
        },
        {
            'text': "Could you walk me through a full stack application you built, detailing your technology choices for both frontend and backend?",
            'difficulty': 'Medium',
            'topic': 'Projects',
            'question_type': 'Project',
            'keywords': ['built', 'project', 'stack', 'node', 'python', 'react', 'postgres', 'mongo']
        },
        {
            'text': "How do you structure your build and deployment process when shipping both frontend single-page apps and backend microservices?",
            'difficulty': 'Hard',
            'topic': 'DevOps',
            'question_type': 'Situational',
            'keywords': ['deploy', 'docker', 'ci/cd', 'github actions', 'heroku', 'aws', 'vercel']
        }
    ],

    'Java Developer': [
        {
            'text': "Could you explain the JVM memory model, particularly how Heap, Stack, and Garbage Collection operate?",
            'difficulty': 'Hard',
            'topic': 'Java Architecture',
            'question_type': 'Technical',
            'keywords': ['jvm', 'heap', 'stack', 'garbage collection', 'gc', 'memory']
        },
        {
            'text': "In Java programming, what are the distinct uses of final, finally, and finalize?",
            'difficulty': 'Easy',
            'topic': 'Java Core',
            'question_type': 'Technical',
            'keywords': ['final', 'finally', 'finalize', 'keyword', 'class', 'try']
        },
        {
            'text': "How does the Java Collections Framework function, and what are the trade-offs between HashMap and ConcurrentHashMap?",
            'difficulty': 'Medium',
            'topic': 'Collections',
            'question_type': 'Technical',
            'keywords': ['collection', 'list', 'map', 'hashmap', 'concurrenthashmap', 'thread safe']
        },
        {
            'text': "How does Spring Boot dependency injection simplify backend development, and how does auto-configuration work behind the scenes?",
            'difficulty': 'Medium',
            'topic': 'Spring Boot',
            'question_type': 'Technical',
            'keywords': ['spring', 'spring boot', 'autowired', 'bean', 'dependency injection', 'annotation']
        }
    ],

    'Python Developer': [
        {
            'text': "Could you explain Python's memory management, reference counting, and how the Global Interpreter Lock (GIL) affects concurrency?",
            'difficulty': 'Hard',
            'topic': 'Python Core',
            'question_type': 'Technical',
            'keywords': ['python', 'gil', 'memory', 'garbage collector', 'threading', 'multiprocessing']
        },
        {
            'text': "What are Python decorators and generator functions, and in what scenarios do you find them most useful?",
            'difficulty': 'Medium',
            'topic': 'Python Advanced',
            'question_type': 'Technical',
            'keywords': ['decorator', 'generator', 'yield', 'function', 'wrapper', 'iter']
        },
        {
            'text': "Could you explain the difference between mutable and immutable objects in Python with concrete examples?",
            'difficulty': 'Easy',
            'topic': 'Python Core',
            'question_type': 'Technical',
            'keywords': ['list', 'tuple', 'dict', 'mutable', 'immutable', 'string']
        },
        {
            'text': "How do you structure Django ORM models and views, or FastAPI async endpoints, when creating robust web APIs?",
            'difficulty': 'Medium',
            'topic': 'Frameworks',
            'question_type': 'Technical',
            'keywords': ['django', 'flask', 'fastapi', 'model', 'view', 'orm', 'route']
        }
    ],

    'Data Analyst': [
        {
            'text': "When working with raw, messy datasets, what structured steps do you take during data cleaning and preprocessing?",
            'difficulty': 'Easy',
            'topic': 'Data Cleaning',
            'question_type': 'Technical',
            'keywords': ['data cleaning', 'null', 'missing', 'duplicate', 'outlier', 'pandas']
        },
        {
            'text': "How do you construct SQL queries using GROUP BY, HAVING, and aggregate functions to extract business insights?",
            'difficulty': 'Medium',
            'topic': 'SQL',
            'question_type': 'Technical',
            'keywords': ['sql', 'group by', 'having', 'count', 'sum', 'avg', 'query']
        },
        {
            'text': "Could you explain the practical differences between SQL JOIN types like INNER, LEFT, and RIGHT joins?",
            'difficulty': 'Medium',
            'topic': 'SQL',
            'question_type': 'Technical',
            'keywords': ['join', 'inner join', 'left join', 'right join', 'foreign key', 'table']
        },
        {
            'text': "How do you handle missing values or extreme outliers when performing statistical analysis on numerical data?",
            'difficulty': 'Medium',
            'topic': 'Statistics',
            'question_type': 'Problem Solving',
            'keywords': ['imputation', 'mean', 'median', 'mode', 'outlier', 'box plot', 'z-score']
        },
        {
            'text': "Could you tell me about an interactive dashboard or data visualization project you designed to communicate metrics?",
            'difficulty': 'Medium',
            'topic': 'Visualization',
            'question_type': 'Project',
            'keywords': ['dashboard', 'tableau', 'power bi', 'chart', 'plot', 'seaborn', 'matplotlib']
        }
    ],

    'Data Scientist': [
        {
            'text': "Could you explain the fundamental distinction between Supervised and Unsupervised Machine Learning algorithms?",
            'difficulty': 'Easy',
            'topic': 'Machine Learning',
            'question_type': 'Technical',
            'keywords': ['supervised', 'unsupervised', 'classification', 'regression', 'clustering', 'label']
        },
        {
            'text': "What causes model overfitting, and what techniques like L1/L2 regularization or cross-validation do you use to prevent it?",
            'difficulty': 'Medium',
            'topic': 'Model Evaluation',
            'question_type': 'Technical',
            'keywords': ['overfitting', 'underfitting', 'regularization', 'lasso', 'ridge', 'cross validation']
        },
        {
            'text': "When accuracy alone is misleading, what evaluation metrics like Precision, Recall, and ROC-AUC do you rely on?",
            'difficulty': 'Medium',
            'topic': 'Evaluation Metrics',
            'question_type': 'Technical',
            'keywords': ['precision', 'recall', 'f1 score', 'roc', 'auc', 'confusion matrix']
        },
        {
            'text': "Could you walk me through an end-to-end Data Science project you built, from feature engineering down to model deployment?",
            'difficulty': 'Hard',
            'topic': 'Projects',
            'question_type': 'Project',
            'keywords': ['pipeline', 'feature engineering', 'model', 'scikit-learn', 'pandas', 'deploy']
        }
    ],

    'Machine Learning Engineer': [
        {
            'text': "How do you construct scalable feature engineering pipelines when preparing large-scale datasets for ML training?",
            'difficulty': 'Medium',
            'topic': 'Feature Engineering',
            'question_type': 'Technical',
            'keywords': ['feature', 'pipeline', 'scaler', 'one hot', 'encoding', 'preprocessing']
        },
        {
            'text': "Could you explain gradient descent optimization algorithms and how you approach hyperparameter tuning?",
            'difficulty': 'Hard',
            'topic': 'Optimization',
            'question_type': 'Technical',
            'keywords': ['gradient descent', 'learning rate', 'grid search', 'optuna', 'adam', 'loss']
        },
        {
            'text': "How do you serve machine learning models in production environments to maintain ultra-low latency inference?",
            'difficulty': 'Hard',
            'topic': 'MLOps',
            'question_type': 'System Design',
            'keywords': ['serve', 'mlops', 'onnx', 'triton', 'fastapi', 'docker', 'latency', 'inference']
        }
    ],

    'AI Engineer': [
        {
            'text': "Could you explain how Transformer architectures and self-attention mechanisms power modern Large Language Models?",
            'difficulty': 'Hard',
            'topic': 'Deep Learning',
            'question_type': 'Technical',
            'keywords': ['transformer', 'attention', 'llm', 'gpt', 'bert', 'embeddings']
        },
        {
            'text': "What is Retrieval-Augmented Generation (RAG), and how do vector databases help ground AI model responses in real data?",
            'difficulty': 'Hard',
            'topic': 'Generative AI',
            'question_type': 'Technical',
            'keywords': ['rag', 'vector database', 'chroma', 'pinecone', 'langchain', 'embedding', 'prompt']
        },
        {
            'text': "How do you evaluate generative AI outputs and guard against hallucinations in production systems?",
            'difficulty': 'Medium',
            'topic': 'AI Evaluation',
            'question_type': 'Problem Solving',
            'keywords': ['hallucination', 'evaluation', 'prompt engineering', 'system prompt', 'temperature']
        }
    ],

    'Cybersecurity Analyst': [
        {
            'text': "Could you explain the CIA Triad—Confidentiality, Integrity, and Availability—and how it guides your security posture?",
            'difficulty': 'Easy',
            'topic': 'Security Fundamentals',
            'question_type': 'Technical',
            'keywords': ['cia triad', 'confidentiality', 'integrity', 'availability', 'security']
        },
        {
            'text': "What is the key difference between Symmetric and Asymmetric Encryption, and where is each applied?",
            'difficulty': 'Medium',
            'topic': 'Cryptography',
            'question_type': 'Technical',
            'keywords': ['encryption', 'symmetric', 'asymmetric', 'rsa', 'aes', 'public key', 'private key']
        },
        {
            'text': "If you suspect an application endpoint is vulnerable to SQL Injection or XSS, how would you investigate and remediate it?",
            'difficulty': 'Hard',
            'topic': 'Application Security',
            'question_type': 'Situational',
            'keywords': ['sql injection', 'xss', 'vulnerability', 'sanitize', 'owasp', 'penetration']
        }
    ],

    'Database Administrator': [
        {
            'text': "Could you explain database indexing strategies and how B-Tree indexes speed up SQL query execution?",
            'difficulty': 'Medium',
            'topic': 'Indexing',
            'question_type': 'Technical',
            'keywords': ['index', 'b-tree', 'query', 'execution plan', 'performance', 'scan']
        },
        {
            'text': "What are ACID properties in relational databases, and how do database engines enforce transactional consistency?",
            'difficulty': 'Medium',
            'topic': 'Transactions',
            'question_type': 'Technical',
            'keywords': ['acid', 'atomicity', 'consistency', 'isolation', 'durability', 'transaction', 'rollback']
        },
        {
            'text': "How do you manage database backups, point-in-time recovery, and replication in high-availability environments?",
            'difficulty': 'Hard',
            'topic': 'DBA Operations',
            'question_type': 'Situational',
            'keywords': ['backup', 'disaster recovery', 'replication', 'master slave', 'sharding', 'failover']
        }
    ],

    'General HR / Behavioral': [
        {
            'text': "Good morning! Could you tell me a little about yourself, your background, and what drew you to this opportunity?",
            'difficulty': 'Easy',
            'topic': 'Behavioral',
            'question_type': 'Behavioral',
            'keywords': ['background', 'experience', 'interests', 'career', 'role']
        },
        {
            'text': "Could you share an example of a challenging situation you encountered in a team setting and how you worked to resolve it?",
            'difficulty': 'Medium',
            'topic': 'Teamwork',
            'question_type': 'Behavioral',
            'keywords': ['conflict', 'team', 'challenge', 'disagreement', 'communication']
        },
        {
            'text': "Where do you see your career path evolving over the next three to five years?",
            'difficulty': 'Easy',
            'topic': 'Career Goals',
            'question_type': 'Behavioral',
            'keywords': ['future', 'goals', 'five years', 'growth', 'aspire']
        }
    ]
}

# Normalize alias map for role lookup
ROLE_ALIAS_MAP = {
    'software developer': 'Software Developer',
    'software engineer': 'Software Developer',
    'frontend developer': 'Frontend Developer',
    'frontend engineer': 'Frontend Developer',
    'backend developer': 'Backend Developer',
    'backend engineer': 'Backend Developer',
    'full stack developer': 'Full Stack Developer',
    'full stack engineer': 'Full Stack Developer',
    'java developer': 'Java Developer',
    'python developer': 'Python Developer',
    'data analyst': 'Data Analyst',
    'data scientist': 'Data Scientist',
    'machine learning engineer': 'Machine Learning Engineer',
    'ml engineer': 'Machine Learning Engineer',
    'ai engineer': 'AI Engineer',
    'cybersecurity analyst': 'Cybersecurity Analyst',
    'security analyst': 'Cybersecurity Analyst',
    'database administrator': 'Database Administrator',
    'dba': 'Database Administrator',
    'hr': 'General HR / Behavioral',
    'behavioral': 'General HR / Behavioral',
}

# Natural Conversational Prefixes & Transitions
CONVERSATIONAL_PREFIXES = [
    "That's interesting. ",
    "Okay, I understand. ",
    "Could you tell me a little more about that? ",
    "You mentioned something relevant there. ",
    "That makes sense. ",
    "Let's look at that from another angle. ",
    "Alright, let's explore that further. ",
    "That's helpful context. "
]

# -----------------------------------------------------------------------------
# Text Normalization & Semantic Similarity Utility
# -----------------------------------------------------------------------------

def normalize_text(text):
    """Clean and normalize string for comparison."""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    return " ".join(words)

def check_semantic_similarity(q1_text, q2_text, threshold=0.68):
    """
    Checks if two question texts are substantially similar using normalized n-grams,
    character sequence matching, and key phrase overlap.
    """
    n1 = normalize_text(q1_text)
    n2 = normalize_text(q2_text)
    
    if not n1 or not n2:
        return False
        
    if n1 == n2:
        return True
        
    # Sequence ratio
    seq_ratio = SequenceMatcher(None, n1, n2).ratio()
    if seq_ratio >= threshold:
        return True
        
    # Word set overlap
    words1 = set(n1.split())
    words2 = set(n2.split())
    
    # Filter common stop words
    stops = {'the', 'a', 'an', 'is', 'are', 'what', 'how', 'explain', 'describe', 'you', 'your', 'can', 'in', 'of', 'and', 'to', 'for', 'with', 'thats', 'okay'}
    w1_sub = words1 - stops
    w2_sub = words2 - stops
    
    if w1_sub and w2_sub:
        jaccard = len(w1_sub.intersection(w2_sub)) / float(len(w1_sub.union(w2_sub)))
        if jaccard >= 0.60:
            return True
            
    return False

# -----------------------------------------------------------------------------
# Entity Extraction & Varied Contextual Interruption System
# -----------------------------------------------------------------------------

TECHNICAL_ENTITIES = {
    'django': 'Django',
    'flask': 'Flask',
    'fastapi': 'FastAPI',
    'react': 'React',
    'vue': 'Vue',
    'angular': 'Angular',
    'express': 'Express',
    'node': 'Node.js',
    'next.js': 'Next.js',
    'nextjs': 'Next.js',
    'python': 'Python',
    'java': 'Java',
    'javascript': 'JavaScript',
    'typescript': 'TypeScript',
    'c++': 'C++',
    'sql': 'SQL',
    'postgresql': 'PostgreSQL',
    'postgres': 'PostgreSQL',
    'mysql': 'MySQL',
    'mongodb': 'MongoDB',
    'redis': 'Redis',
    'sqlite': 'SQLite',
    'git': 'Git',
    'docker': 'Docker',
    'kubernetes': 'Kubernetes',
    'pytorch': 'PyTorch',
    'tensorflow': 'TensorFlow',
    'pandas': 'Pandas',
    'numpy': 'NumPy',
    'rest': 'REST API',
    'api': 'APIs',
    'microservices': 'Microservices',
    'jwt': 'JWT Authentication',
    'oauth': 'OAuth',
    'oop': 'OOP design',
    'dsa': 'Data Structures & Algorithms',
    'redux': 'Redux state management',
    'ci/cd': 'CI/CD pipelines',
}

def extract_transcript_entities(transcript):
    """Extracts technical terms, tools, frameworks, and project claims from candidate answer."""
    if not transcript:
        return []
    text_lower = transcript.lower()
    found = []
    for key, display_name in TECHNICAL_ENTITIES.items():
        if re.search(r'\b' + re.escape(key) + r'\b', text_lower):
            if display_name not in found:
                found.append(display_name)
    return found

INTERRUPTIONS_LIBRARY = [
    {
        'type': 'clarification',
        'prompt': "Could you explain that technical concept in simpler, more practical terms?"
    },
    {
        'type': 'technical',
        'prompt': "Can you walk me through a concrete code example or design decision for that?"
    },
    {
        'type': 'challenge',
        'prompt': "Why did you choose that specific approach over alternative frameworks or architecture designs?"
    },
    {
        'type': 'follow_up',
        'prompt': "What would be your immediate debugging steps if that solution threw a runtime exception in production?"
    },
    {
        'type': 'pressure',
        'prompt': "Summarize the key engineering outcome of your solution in one clear sentence."
    },
    {
        'type': 'scenario',
        'prompt': "Suppose server traffic increases tenfold overnight. How does your solution hold up?"
    },
    {
        'type': 'evidence',
        'prompt': "What specific parts of that implementation did you personally write versus inheriting?"
    },
    {
        'type': 'deeper_reasoning',
        'prompt': "What underlying mechanism makes you confident that approach is optimal?"
    },
    {
        'type': 'alternative',
        'prompt': "If you were forbidden from using that tool or library, how else would you build it?"
    }
]

def get_next_interruption(session, last_transcript=""):
    """
    Selects or constructs candidate-aware interruptions referencing candidate statements,
    avoiding repetition within the same session.
    """
    used_interruptions = list(getattr(session, 'used_interruptions_json', []) or [])
    
    # Try entity-specific contextual interruption if candidate mentioned technologies
    entities = extract_transcript_entities(last_transcript)
    if entities:
        main_entity = entities[0]
        contextual_prompts = [
            (f"context_{main_entity.lower()}_arch", f"You mentioned using {main_entity}. What part of the {main_entity} architecture did you personally design?"),
            (f"context_{main_entity.lower()}_tradeoff", f"You mentioned {main_entity}. What was the biggest technical tradeoff you encountered while using it?"),
            (f"context_{main_entity.lower()}_opt", f"Regarding {main_entity}, how did you optimize performance or handle errors in production?")
        ]
        for c_type, c_prompt in contextual_prompts:
            if c_type not in used_interruptions:
                used_interruptions.append(c_type)
                session.used_interruptions_json = used_interruptions
                session.save(update_fields=['used_interruptions_json'])
                return {'type': c_type, 'prompt': c_prompt}

    available = [item for item in INTERRUPTIONS_LIBRARY if item['type'] not in used_interruptions]
    
    if not available:
        used_interruptions = []
        available = list(INTERRUPTIONS_LIBRARY)
        
    selected = random.choice(available)
    
    used_interruptions.append(selected['type'])
    session.used_interruptions_json = used_interruptions
    session.save(update_fields=['used_interruptions_json'])
    
    return selected

# -----------------------------------------------------------------------------
# Adaptive Job Role Question Generator & Fallback Engine
# -----------------------------------------------------------------------------

def get_role_pool(job_role):
    """Retrieve pool for the given role string with fallback."""
    if not job_role:
        return JOB_ROLE_QUESTION_POOLS['Software Developer']
        
    clean_role = job_role.strip().lower()
    canonical_role = ROLE_ALIAS_MAP.get(clean_role)
    
    if canonical_role and canonical_role in JOB_ROLE_QUESTION_POOLS:
        return JOB_ROLE_QUESTION_POOLS[canonical_role]
        
    for key, pool in JOB_ROLE_QUESTION_POOLS.items():
        if key.lower() in clean_role or clean_role in key.lower():
            return pool
            
    return JOB_ROLE_QUESTION_POOLS['Software Developer']

def is_question_used(candidate_q_text, used_questions_list):
    """Checks if candidate_q_text matches any in used_questions_list exact or semantically."""
    for used_q in used_questions_list:
        if check_semantic_similarity(candidate_q_text, used_q):
            return True
    return False

def select_next_question_for_session(session, last_transcript=""):
    """
    Generates/Selects the next job-role specific question using full history,
    semantic deduplication, 10 follow-up strategies, entity extraction, and guaranteed fallbacks.
    """
    job_role = getattr(session, 'job_role', 'Software Developer') or 'Software Developer'
    pool = get_role_pool(job_role)
    
    current_used = list(getattr(session, 'used_questions_json', []) or [])
    
    from ..models import InterviewSession
    recent_sessions = InterviewSession.objects.filter(
        user=session.user
    ).exclude(id=session.id).order_by('-created_at')[:5]
    
    history_questions = list(current_used)
    for past_s in recent_sessions:
        past_used = getattr(past_s, 'used_questions_json', []) or []
        history_questions.extend(past_used)

    unused_pool = [q for q in pool if not is_question_used(q['text'], history_questions)]

    # Initial Question (Q1) Conversational Greeting
    if len(current_used) == 0:
        user_bio = getattr(getattr(session.user, 'profile', None), 'bio', '') or ''
        
        q1_options = [
            f"Good morning! Let's start with something simple. Could you tell me a little about yourself and what you've been working on recently?",
            f"Welcome to your interview today! To get us started, could you introduce yourself and walk me through your background in {job_role} development?",
            f"Hello! I'm glad to meet you. Could you give me a brief overview of your technical background and key projects as a {job_role}?"
        ]
        
        unused_q1 = [q for q in q1_options if q not in history_questions]
        
        if ("django" in user_bio.lower() or "python" in user_bio.lower()) and "django" not in [h.lower() for h in history_questions]:
            selected_text = f"Good morning! I noticed from your profile that you've worked with Python and Django. Could you tell me a little about yourself and how you've used those technologies in your {job_role} projects?"
        elif unused_q1:
            selected_text = unused_q1[0]
        elif unused_pool:
            raw_q = unused_pool[0]['text']
            selected_text = f"Welcome! Let's begin. {raw_q}"
        else:
            selected_text = f"Welcome! To start our {job_role} interview, could you share a brief summary of your core technical skills and experience?"
            
        current_used.append(selected_text)
        session.used_questions_json = current_used
        session.save(update_fields=['used_questions_json'])
        return selected_text

    # 1. ADAPTIVE 10-STRATEGY FOLLOW-UP based on candidate transcript & extracted entities
    adaptive_question = None
    if last_transcript and last_transcript.strip() and len(last_transcript.strip()) > 10:
        transcript_lower = last_transcript.lower()
        entities = extract_transcript_entities(last_transcript)
        
        disclaim_keywords = ["don't know", "dont know", "not sure", "no experience", "haven't used", "never worked"]
        candidate_disclaimed = any(dk in transcript_lower for dk in disclaim_keywords)
        
        if not candidate_disclaimed:
            # Match keywords against unused pool items
            matching_adaptive = []
            for q_item in unused_pool:
                for kw in q_item.get('keywords', []):
                    if kw in transcript_lower:
                        matching_adaptive.append((q_item, kw))
                        break
                        
            if matching_adaptive:
                best_match_q = random.choice(matching_adaptive)[0]
                prefix = random.choice(CONVERSATIONAL_PREFIXES)
                adaptive_question = prefix + best_match_q['text']
            elif entities:
                ent = entities[0]
                # Pick strategy dynamically based on question position
                strategy_idx = len(current_used) % 10
                strategies = [
                    f"That's interesting. You mentioned {ent}. Could you clarify the specific architecture or design patterns you used with {ent}?",
                    f"Okay, I understand. Why did you choose {ent} for your implementation rather than alternative tools or libraries?",
                    f"Going deeper into your experience with {ent}, how does your code handle performance bottlenecks or memory management?",
                    f"Could you share a practical production example where you applied {ent} to solve a complex problem?",
                    f"When encountering unexpected errors or bugs while working with {ent}, what was your exact troubleshooting process?",
                    f"How would you compare {ent} against other options in terms of scalability and developer efficiency?",
                    f"In a high-load scenario involving {ent}, how would you architect the data flow and error recovery?",
                    f"What specific debugging tools or techniques do you rely on most when diagnosing issues in {ent}?",
                    f"What was your specific ownership role when implementing solutions using {ent}?",
                    f"What was the most challenging technical tradeoff you faced when integrating {ent}?"
                ]
                adaptive_question = strategies[strategy_idx]
            elif "project" in transcript_lower or "built" in transcript_lower or "app" in transcript_lower:
                adaptive_question = "I noticed you mentioned working on a project. Could you walk me through what you built, your architecture choices, and your personal contribution?"

    if adaptive_question and not is_question_used(adaptive_question, current_used):
        selected_text = adaptive_question
    # 2. UNUSED QUESTION FROM SELECTED JOB ROLE POOL
    elif unused_pool:
        raw_q = random.choice(unused_pool)['text']
        prefix = random.choice(CONVERSATIONAL_PREFIXES) if len(current_used) > 0 else ""
        selected_text = prefix + raw_q
    # 3. UNUSED QUESTION FROM ANY JOB ROLE POOL
    else:
        all_pool_questions = []
        for r_name, r_pool in JOB_ROLE_QUESTION_POOLS.items():
            for q_item in r_pool:
                if not is_question_used(q_item['text'], current_used):
                    all_pool_questions.append(q_item['text'])
                    
        if all_pool_questions:
            raw_q = random.choice(all_pool_questions)
            prefix = random.choice(CONVERSATIONAL_PREFIXES)
            selected_text = prefix + raw_q
        # 4. SAFE PREDEFINED CATEGORY FALLBACK (Guaranteed Non-Null)
        else:
            fallback_options = [
                f"Okay, I understand. Looking at your role as a {job_role}, how do you usually approach solving complex engineering problems?",
                f"That's helpful context. What is a key technical project you completed recently as a {job_role}?",
                f"Could you explain your typical workflow for testing and debugging your code?",
                f"How do you keep your technical skills updated in {job_role} development?",
                f"Describe how you collaborate with team members on technical deliverables."
            ]
            unused_fallbacks = [fb for fb in fallback_options if fb not in current_used]
            if unused_fallbacks:
                selected_text = unused_fallbacks[0]
            else:
                selected_text = f"Could you describe your key technical strengths as a {job_role}?"

    current_used.append(selected_text)
    session.used_questions_json = current_used
    session.save(update_fields=['used_questions_json'])
    
    return selected_text
