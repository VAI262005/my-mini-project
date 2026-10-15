"""
Comprehensive Learning Center Initial Data & Seeding Utility
Covers all 18 placement preparation categories with rich educational topics.
"""

LEARNING_DATA = [
    {
        'name': 'Interview Basics',
        'slug': 'interview-basics',
        'icon': 'fa-id-card',
        'category_type': 'general',
        'order': 1,
        'description': 'Essential foundations for preparing before, during, and after an interview.',
        'topics': [
            {
                'title': 'How to Introduce Yourself ("Tell Me About Yourself")',
                'slug': 'how-to-introduce-yourself',
                'difficulty': 'Beginner',
                'summary': 'Structure your 60-90 second professional elevator pitch effectively.',
                'explanation': 'Your introduction sets the tone for the entire interview. Focus on the PRESENT (current status & degree), PAST (key projects & internships), and FUTURE (why you are excited about this specific role). Keep it focused on relevant technical and problem-solving experience rather than personal hobbies.',
                'real_world_example': 'Instead of listing your entire schooling history, state your degree, mention 2 major web or machine learning projects, 1 internship experience, and why you want to apply your skills here.',
                'interview_question': 'Tell me about yourself and your technical background.',
                'sample_answer': 'Good morning! I am a final-year Computer Science student passionate about full-stack web development and database design. Recently, I built an AI-driven interview feedback application using Django and JavaScript. During my internship at TechCorp, I optimized SQL queries that reduced load times by 25%. I am excited to apply my problem-solving skills to scalable software solutions at your company.',
                'common_mistake': 'Making the introduction too long (over 3 minutes) or repeating your entire resume line-by-line.',
                'practical_tip': 'Keep your introduction between 60 to 90 seconds. Speak at a moderate, calm pace.',
                'practice_question': 'What is the optimal duration for a candidate introduction in a technical interview?',
                'practice_options_json': ['30 seconds', '60 to 90 seconds', '4 to 5 minutes', 'As long as possible'],
                'correct_option_index': 1
            },
            {
                'title': 'How to Handle Questions You Don\'t Know',
                'slug': 'handling-unknown-questions',
                'difficulty': 'Intermediate',
                'summary': 'Stay calm, think aloud, and avoid guessing blindly when stumped.',
                'explanation': 'Interviewers often ask questions at the edge of your knowledge to test your problem-solving under uncertainty. Never say "I don\'t know" immediately or try to fake an answer. Instead, acknowledge what you do know, break down the problem logically, and share your reasoning.',
                'real_world_example': 'If asked about Redis clustering and you\'ve only used single-node Redis, say: "I haven\'t configured multi-node Redis clusters in production yet, but based on caching principles and horizontal scaling, I would approach it by partitioning keys..."',
                'interview_question': 'How do you handle a complex technical question when you don\'t immediately know the answer?',
                'sample_answer': 'I don\'t panic or guess blindly. First, I ask clarifying questions to ensure I understand the requirements. Then I explain my thought process out loud using fundamentals I know, and ask if I can walk through a logical solution together.',
                'common_mistake': 'Pretending to know the concept and giving a completely wrong or fabricated definition.',
                'practical_tip': 'Use the phrasing: "I haven\'t worked with that specific library directly, but based on core principles of X, I would approach it by..."',
                'practice_question': 'Which candidate response is best when asked about an unfamiliar framework?',
                'practice_options_json': [
                    'Immediately say "I don\'t know" and wait for the next question.',
                    'Make up a definition and hope the interviewer doesn\'t notice.',
                    'State your related foundational knowledge and think aloud logically.',
                    'Argue that the technology is obsolete anyway.'
                ],
                'correct_option_index': 2
            }
        ]
    },
    {
        'name': 'HR Interview',
        'slug': 'hr-interview',
        'icon': 'fa-users',
        'category_type': 'hr',
        'order': 2,
        'description': 'Master behavioral, situational, and HR round placement questions.',
        'topics': [
            {
                'title': 'What Are Your Strengths and Weaknesses?',
                'slug': 'strengths-and-weaknesses',
                'difficulty': 'Beginner',
                'summary': 'Highlight authentic technical strengths and genuine, non-fatal areas of improvement.',
                'explanation': 'For strengths, provide concrete evidence (e.g., persistence in debugging, quick adaptability to new frameworks). For weaknesses, pick a real technical area you are actively working to improve (e.g., public speaking, over-engineering initial solutions) and detail the exact steps you are taking to fix it.',
                'real_world_example': 'Weakness: "In early projects, I spent too much time perfecting code before getting user feedback. Now I build working MVPs first and iterate based on testing."',
                'interview_question': 'What is your greatest technical weakness and how are you addressing it?',
                'sample_answer': 'My biggest area for growth has been delegating tasks during group projects because I tend to take on backend implementation myself. To address this, I started using Jira boards and sprint planning to distribute modules evenly among team members.',
                'common_mistake': 'Saying "I am a perfectionist" or "I work too hard" (cliché) or naming a critical core job skill as a weakness.',
                'practical_tip': 'Always pair your weakness with the active corrective action you are taking.',
                'practice_question': 'What should always accompany a weakness mentioned in an interview?',
                'practice_options_json': [
                    'An excuse blaming previous teammates.',
                    'The actionable steps you are taking to improve it.',
                    'A disclaimer that you will never change.',
                    'A joke to distract the interviewer.'
                ],
                'correct_option_index': 1
            },
            {
                'title': 'Why Should We Hire You?',
                'slug': 'why-should-we-hire-you',
                'difficulty': 'Intermediate',
                'summary': 'Align your skills, technical portfolio, and growth mindset with the company\'s goals.',
                'explanation': 'Connect your technical background directly to the company\'s tech stack and domain. Show enthusiasm, highlight your fast learning ability, and explain how your projects demonstrate initiative.',
                'real_world_example': 'If the company uses Python and Cloud services, highlight your hands-on Django projects and API development experience.',
                'interview_question': 'Why should our development team hire you over other candidates?',
                'sample_answer': 'You should hire me because I bring both strong computer science fundamentals and practical full-stack project experience. I have built end-to-end web applications, automated unit testing, and possess a proven drive to learn new tools quickly as demonstrated in my recent placement projects.',
                'common_mistake': 'Giving generic answers like "Because I am hard working and need a job."',
                'practical_tip': 'Focus on the value you add to the team, not just what the job does for you.',
                'practice_question': 'What is the most effective element to include when answering "Why should we hire you?"',
                'practice_options_json': [
                    'Your personal financial needs.',
                    'Concrete examples of relevant projects and problem-solving skills.',
                    'A promise that you will work 24/7 without breaks.',
                    'Complaints about other companies.'
                ],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Technical Interview',
        'slug': 'technical-interview',
        'icon': 'fa-code-branch',
        'category_type': 'technical',
        'order': 3,
        'description': 'Core computer science fundamentals, OOP principles, and system concepts.',
        'topics': [
            {
                'title': 'Object-Oriented Programming (OOP) Pillars',
                'slug': 'oop-pillars',
                'difficulty': 'Intermediate',
                'summary': 'Understand Encapsulation, Inheritance, Polymorphism, and Abstraction.',
                'explanation': 'OOP is a programming paradigm based on objects containing data (attributes) and code (methods). The 4 key pillars are:\n1. Encapsulation: Bundling data and methods into a single class and restricting direct access.\n2. Inheritance: Mechanism where a child class acquires properties of a parent class.\n3. Polymorphism: Ability of methods to take different forms (Method Overloading & Overriding).\n4. Abstraction: Hiding internal implementation details and showing only essential functionality.',
                'real_world_example': 'A Smartphone class hides its internal circuit board details (Abstraction), exposes volume buttons (Interface), inherits from a basic Phone class (Inheritance), and changes volume behavior based on audio mode (Polymorphism).',
                'interview_question': 'Explain the difference between Abstraction and Encapsulation with an example.',
                'sample_answer': 'Abstraction is about hiding internal complexity and showing only essential features (like a car dashboard), whereas Encapsulation is about binding data and methods together into a class while restricting direct variable access using private modifiers.',
                'common_mistake': 'Confusing Abstraction with Encapsulation during explanation.',
                'practical_tip': 'Remember: Encapsulation = Data Hiding & Packaging. Abstraction = Implementation Hiding.',
                'practice_question': 'Which OOP pillar restricts direct internal access to object attributes?',
                'practice_options_json': ['Polymorphism', 'Inheritance', 'Encapsulation', 'Abstraction'],
                'correct_option_index': 2
            },
            {
                'title': 'Array vs Linked List Data Structure Trade-offs',
                'slug': 'array-vs-linked-list',
                'difficulty': 'Intermediate',
                'summary': 'Compare memory layout, lookup speed, and insertion/deletion complexities.',
                'explanation': 'Arrays store elements in contiguous memory locations allowing O(1) random access by index, but insertions/deletions require shifting (O(N)). Linked Lists use non-contiguous memory connected via pointers/references, making insertions/deletions at known nodes O(1), but random access requires traversal (O(N)).',
                'real_world_example': 'Use an Array when you need frequent random access to lookup elements by position. Use a Linked List when you perform frequent insertions and deletions at the head/tail.',
                'interview_question': 'When would you prefer a Linked List over an Array in a software application?',
                'sample_answer': 'I would prefer a Linked List when dynamic size changes and frequent insertions or deletions at arbitrary positions occur without requiring random indexing access, avoiding contiguous memory reallocation costs.',
                'common_mistake': 'Assuming Linked Lists are always faster than Arrays. Arrays have far better CPU cache locality.',
                'practical_tip': 'Mention cache locality: Arrays benefit from CPU caching due to contiguous memory allocation.',
                'practice_question': 'What is the time complexity of looking up an element by index in a standard array?',
                'practice_options_json': ['O(N)', 'O(1)', 'O(log N)', 'O(N^2)'],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Programming',
        'slug': 'programming',
        'icon': 'fa-laptop-code',
        'category_type': 'coding',
        'order': 4,
        'description': 'Master core programming fundamentals, memory handling, and exception logic.',
        'topics': [
            {
                'title': 'Exception Handling Best Practices',
                'slug': 'exception-handling',
                'difficulty': 'Beginner',
                'summary': 'Handle runtime errors gracefully using try-catch blocks without swallowing exceptions.',
                'explanation': 'Exception handling prevents unexpected application crashes by catching runtime errors. Always catch specific exceptions (e.g. ValueError, FileNotFoundError) rather than catching bare Exceptions, log error details, and clean up resources in a finally block.',
                'real_world_example': 'When opening a database connection or reading a file, use try-except-finally or context managers (with open(...) as f) to ensure resources are released even if an error occurs.',
                'interview_question': 'Why is catching bare Exception considered a bad practice in software engineering?',
                'sample_answer': 'Catching bare Exception masks bugs (including syntax errors, KeyboardInterrupts, or system exits) and makes debugging extremely difficult because unexpected exceptions fail silently without proper diagnostic tracebacks.',
                'common_mistake': 'Using empty try-except blocks that silently swallow all exceptions.',
                'practical_tip': 'Use language context managers (like Python\'s `with` statement) to handle cleanup automatically.',
                'practice_question': 'What block in Python/Java is guaranteed to run whether an exception occurs or not?',
                'practice_options_json': ['try', 'except / catch', 'finally', 'else'],
                'correct_option_index': 2
            }
        ]
    },
    {
        'name': 'DSA',
        'slug': 'dsa',
        'icon': 'fa-sitemap',
        'category_type': 'coding',
        'order': 5,
        'description': 'Data structures and algorithm optimization techniques.',
        'topics': [
            {
                'title': 'Two Pointer Technique',
                'slug': 'two-pointer-technique',
                'difficulty': 'Intermediate',
                'summary': 'Optimize array and string traversal from O(N^2) down to O(N).',
                'explanation': 'The Two Pointer technique uses two indices (pointers) to traverse a data structure simultaneously, typically moving from opposite ends toward the center (e.g., binary search, two-sum on sorted arrays) or at different speeds (fast/slow pointers for cycle detection).',
                'real_world_example': 'Checking if a string is a palindrome by comparing left and right pointers moving inward.',
                'interview_question': 'How does the two-pointer technique reduce time complexity for Two Sum on a sorted array?',
                'sample_answer': 'On a sorted array, placing one pointer at start and one at end allows us to check the sum. If the sum is greater than target, we decrement the right pointer; if smaller, we increment the left pointer. This scans the array in linear O(N) time instead of nested O(N^2) loops.',
                'common_mistake': 'Applying two pointers on an unsorted array without sorting first when order matters.',
                'practical_tip': 'When asked to optimize nested loops on arrays or strings, check if two pointers or sliding window applies.',
                'practice_question': 'What is the time complexity of two-pointer traversal on an N-length sorted array?',
                'practice_options_json': ['O(N^2)', 'O(N)', 'O(log N)', 'O(2^N)'],
                'correct_option_index': 1
            },
            {
                'title': 'Sliding Window Technique',
                'slug': 'sliding-window-technique',
                'difficulty': 'Intermediate',
                'summary': 'Efficiently compute subarray/substring problems using contiguous window bounds.',
                'explanation': 'The Sliding Window technique tracks a window over an array/string that expands or shrinks based on constraints. Fixed window size maintains a set length; dynamic window expands right until invalid, then shrinks left.',
                'real_world_example': 'Finding the maximum sum of K consecutive elements in an array or finding the longest substring without repeating characters.',
                'interview_question': 'What is the advantage of Sliding Window over brute-force subarray evaluation?',
                'sample_answer': 'Brute force checks all subarrays taking O(N * K) or O(N^2) time. Sliding Window reuses redundant calculations by adding the incoming right element and subtracting the outgoing left element in O(1) step, reducing total complexity to linear O(N).',
                'common_mistake': 'Recomputing the sum or state of the entire window at each step instead of incrementally updating it.',
                'practical_tip': 'Use sliding window when the problem involves contiguous subarrays or substrings with sum/length conditions.',
                'practice_question': 'In a sliding window algorithm, how is the sum updated when shifting a fixed window of size K to the right?',
                'practice_options_json': [
                    'Recompute the sum of all K elements from scratch.',
                    'Multiply the sum by K.',
                    'Add the new right element and subtract the old left element.',
                    'Square the new right element.'
                ],
                'correct_option_index': 2
            }
        ]
    },
    {
        'name': 'DBMS & SQL',
        'slug': 'dbms-sql',
        'icon': 'fa-database',
        'category_type': 'technical',
        'order': 6,
        'description': 'Database fundamentals, normalization, SQL joins, and indexing.',
        'topics': [
            {
                'title': 'SQL Joins Explained (INNER, LEFT, RIGHT, FULL)',
                'slug': 'sql-joins-explained',
                'difficulty': 'Beginner',
                'summary': 'Combine records from two or more database tables based on related columns.',
                'explanation': 'SQL Joins retrieve combined data from tables:\n- INNER JOIN: Returns matching rows from both tables.\n- LEFT JOIN: Returns all rows from left table and matching rows from right table (filling NULLs if missing).\n- RIGHT JOIN: Returns all rows from right table and matching rows from left table.\n- FULL OUTER JOIN: Returns all rows when there is a match in either table.',
                'real_world_example': 'An e-commerce site joining `Customers` and `Orders` tables. A LEFT JOIN ensures customers with zero orders still appear in the analytical report.',
                'interview_question': 'What is the main difference between INNER JOIN and LEFT JOIN in SQL?',
                'sample_answer': 'INNER JOIN returns only the records that have matching keys in both tables, omitting unmatched rows. LEFT JOIN returns all rows from the left table regardless of matches, placing NULL values in right-table columns when no match exists.',
                'common_mistake': 'Using INNER JOIN when you need to retain records from the primary table that have no foreign key matches.',
                'practical_tip': 'Visualize joins as Venn diagrams: INNER JOIN is the intersection; LEFT JOIN is the entire left circle.',
                'practice_question': 'If table A has 5 rows and table B has 0 matching rows, how many rows does `A LEFT JOIN B` return?',
                'practice_options_json': ['0', '5', '10', 'NULL'],
                'correct_option_index': 1
            },
            {
                'title': 'Database Normalization (1NF, 2NF, 3NF)',
                'slug': 'database-normalization',
                'difficulty': 'Intermediate',
                'summary': 'Organize database tables to eliminate redundancy and update anomalies.',
                'explanation': 'Normalization structures relational database tables to reduce redundancy:\n- 1NF: Atomic values only; no repeating groups.\n- 2NF: Meets 1NF + all non-key attributes fully depend on the primary key (no partial dependency).\n- 3NF: Meets 2NF + no transitive dependencies (non-key attribute determining another non-key attribute).',
                'real_world_example': 'Storing student details and department location in the same table causes update anomalies if a department moves. Moving department details into a separate `Departments` table enforces 3NF.',
                'interview_question': 'What is transitive dependency and which normal form eliminates it?',
                'sample_answer': 'Transitive dependency occurs when a non-key column depends on another non-key column rather than directly on the primary key (A -> B -> C). 3NF eliminates transitive dependencies by splitting related non-key columns into a distinct table.',
                'common_mistake': 'Over-normalizing to BCNF/5NF in real-world high-read applications where denormalization is intentional for speed.',
                'practical_tip': 'Remember the mnemonic for 3NF: "The key, the whole key, and nothing but the key, so help me Codd."',
                'practice_question': 'Which normal form requires eliminating partial dependencies on a composite primary key?',
                'practice_options_json': ['1NF', '2NF', '3NF', 'BCNF'],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Web Development',
        'slug': 'web-development',
        'icon': 'fa-globe',
        'category_type': 'technical',
        'order': 7,
        'description': 'Frontend, backend, RESTful APIs, Django, and web architecture.',
        'topics': [
            {
                'title': 'REST API Architecture & HTTP Verbs',
                'slug': 'rest-api-architecture',
                'difficulty': 'Beginner',
                'summary': 'Understand RESTful principles, endpoints, statelessness, and HTTP methods.',
                'explanation': 'Representational State Transfer (REST) is an architectural style for web APIs based on stateless server interactions and standard HTTP methods:\n- GET: Retrieve resources.\n- POST: Create a new resource.\n- PUT: Replace/update an entire existing resource.\n- PATCH: Partially update a resource.\n- DELETE: Remove a resource.',
                'real_world_example': 'Fetching user profile data using `GET /api/users/42` and updating user status using `PATCH /api/users/42`.',
                'interview_question': 'What does it mean for a REST API to be stateless?',
                'sample_answer': 'Statelessness means the server does not store candidate session state between requests. Every single client HTTP request must contain all necessary information (such as authentication tokens) for the server to process it independently.',
                'common_mistake': 'Using GET requests for operations that mutate database state.',
                'practical_tip': 'Remember idempotency: GET, PUT, and DELETE should be idempotent (calling multiple times produces the same server state). POST is not idempotent.',
                'practice_question': 'Which HTTP method is designed to perform partial updates on an existing resource?',
                'practice_options_json': ['GET', 'POST', 'PATCH', 'DELETE'],
                'correct_option_index': 2
            }
        ]
    },
    {
        'name': 'AI & Machine Learning',
        'slug': 'ai-machine-learning',
        'icon': 'fa-brain',
        'category_type': 'technical',
        'order': 8,
        'description': 'AI fundamentals, ML paradigms, evaluation metrics, and speech/NLP concepts.',
        'topics': [
            {
                'title': 'Supervised vs Unsupervised Learning',
                'slug': 'supervised-vs-unsupervised-learning',
                'difficulty': 'Beginner',
                'summary': 'Distinguish between labeled target learning and unlabeled pattern discovery.',
                'explanation': 'Supervised learning trains models on labeled input-output pairs to predict target outcomes (Classification & Regression). Unsupervised learning analyzes unlabeled datasets to discover hidden patterns, groupings, or clusters (K-Means, PCA).',
                'real_world_example': 'Supervised: Predicting housing prices (Regression) or classifying email as Spam/Ham (Classification). Unsupervised: Segmenting online shoppers into behavioral groups (Clustering).',
                'interview_question': 'How does model evaluation differ between classification and regression tasks?',
                'sample_answer': 'Classification evaluates categorical predictions using metrics like Accuracy, Precision, Recall, and F1-Score. Regression evaluates continuous numeric outputs using metrics like Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared.',
                'common_mistake': 'Using Accuracy metric on imbalanced classification datasets (e.g. 99% negative cases).',
                'practical_tip': 'When asked about evaluation metrics for imbalanced data, recommend Precision, Recall, and F1-Score over raw Accuracy.',
                'practice_question': 'Which machine learning task involves predicting a continuous numerical value?',
                'practice_options_json': ['Classification', 'Regression', 'Clustering', 'Dimensionality Reduction'],
                'correct_option_index': 1
            },
            {
                'title': 'How Speech & NLP Powers AI Interview Analyzers',
                'slug': 'speech-nlp-interview-analyzers',
                'difficulty': 'Intermediate',
                'summary': 'Connect speech recognition, sentiment analysis, and keyword extraction to local application pipelines.',
                'explanation': 'An AI interview analyzer converts candidate audio to transcript text using Speech-to-Text engines, normalizes words, extracts technical entities, calculates speaking speed (WPM), detects filler word density, and computes relevance scores using natural language processing (NLP).',
                'real_world_example': 'When a candidate speaks "I built Django backends", the speech pipeline transcribes audio, NLP extracts "Django" as a technical entity, and evaluates relevance against the asked question.',
                'interview_question': 'How does an AI system extract technical entities from candidate speech transcripts?',
                'sample_answer': 'The speech signal is transcribed into text using Speech Recognition. Then, NLP pipelines perform tokenization, regular expression keyword matching, and named entity recognition to map candidate phrases against predefined technical domain dictionaries.',
                'common_mistake': 'Confusing Speech Recognition (converting sound to text) with Natural Language Processing (understanding text semantics).',
                'practical_tip': 'Emphasize the modular pipeline: Audio Input -> Speech-to-Text -> Text Preprocessing -> Feature Extraction -> Scoring Engine.',
                'practice_question': 'What is the primary function of a Speech-to-Text engine in an AI interview system?',
                'practice_options_json': [
                    'To calculate video camera eye contact.',
                    'To transcribe spoken candidate audio into machine-readable text.',
                    'To compile Python code syntax.',
                    'To generate SQL database migrations.'
                ],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Communication Skills',
        'slug': 'communication-skills',
        'icon': 'fa-comments',
        'category_type': 'communication',
        'order': 9,
        'description': 'Speaking clarity, reducing filler words, pacing, and concise technical delivery.',
        'topics': [
            {
                'title': 'Eliminating Filler Words & Managing Hesitation Pauses',
                'slug': 'eliminating-filler-words',
                'difficulty': 'Beginner',
                'summary': 'Replace "um", "like", and "basically" with deliberate, confident pauses.',
                'explanation': 'Filler words occur when your brain is formulating ideas faster or slower than your mouth. Replacing fillers with silent 1-second pauses projects composure, clarity, and authority.',
                'real_world_example': 'BAD: "Actually... basically... like... I think maybe Django is good."\nBETTER: "I chose Django because it provides built-in ORM, authentication, and URL routing out of the box."',
                'interview_question': 'How do you maintain composure and avoid filler words when answering under pressure?',
                'sample_answer': 'I pause for a second before answering to organize my thoughts into 2 or 3 bullet points. If I need a moment during an answer, I pause silently rather than making filler sounds like "um" or "like".',
                'common_mistake': 'Rushing to speak immediately before knowing what you want to say.',
                'practical_tip': 'Embrace brief silent pauses. Interviewers perceive silent pauses as thoughtful reflection.',
                'practice_question': 'What is the best alternative to using filler words like "um" or "like" while thinking?',
                'practice_options_json': [
                    'Speaking twice as fast.',
                    'Taking a brief, silent 1-second pause.',
                    'Repeating the question 5 times.',
                    'Apologizing repeatedly.'
                ],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Answer Structuring',
        'slug': 'answer-structuring',
        'icon': 'fa-layer-group',
        'category_type': 'communication',
        'order': 10,
        'description': 'Master STAR (Situation, Task, Action, Result) and PREP frameworks.',
        'topics': [
            {
                'title': 'The STAR Method for Behavioral Questions',
                'slug': 'star-method',
                'difficulty': 'Beginner',
                'summary': 'Structure behavioral responses using Situation, Task, Action, and Result.',
                'explanation': 'The STAR framework ensures clear, structured responses to behavioral questions:\n- S (Situation): Describe the context/background.\n- T (Task): Explain your goal or challenge.\n- A (Action): Detail the exact steps YOU took.\n- R (Result): Share the quantifiable outcome and key learning.',
                'real_world_example': 'Situation: During my final year project, database queries were taking 4 seconds.\nTask: I needed to reduce latency before candidate testing.\nAction: I added composite indexes and refactored ORM queries.\nResult: Page load times dropped to 300ms, improving user experience.',
                'interview_question': 'Walk me through a technical challenge you resolved using the STAR method.',
                'sample_answer': 'Situation: In our team placement portal, concurrent registration requests crashed the database. Task: I was responsible for solving the bottleneck. Action: I implemented a Redis queue and connection pool. Result: The portal handled 500 simultaneous users with zero downtime.',
                'common_mistake': 'Spending 80% of the time describing the situation and only 20% detailing your personal action.',
                'practical_tip': 'Spend 15% on Situation/Task, 60% on YOUR specific Action, and 25% on Result.',
                'practice_question': 'In the STAR method, which component should receive the largest proportion of your answer?',
                'practice_options_json': ['Situation', 'Task', 'Action', 'Result'],
                'correct_option_index': 2
            }
        ]
    },
    {
        'name': 'Body Language',
        'slug': 'body-language',
        'icon': 'fa-user-astronaut',
        'category_type': 'communication',
        'order': 11,
        'description': 'Visible behavioral indicators, eye gaze alignment, posture, and facial expression changes.',
        'topics': [
            {
                'title': 'Webcam Eye Gaze Alignment & Sitting Posture',
                'slug': 'webcam-eye-gaze-posture',
                'difficulty': 'Beginner',
                'summary': 'Maintain professional video presence using visible behavioral alignment techniques.',
                'explanation': 'In online interviews, looking directly at or near the camera lens creates the visible behavioral indicator of eye contact. Maintain an upright posture with shoulders relaxed and hands visible when gesturing.',
                'real_world_example': 'Position your interview camera at eye level so your face and upper chest are clearly visible in the webcam preview.',
                'interview_question': 'Why is camera alignment important during an online technical AI interview?',
                'sample_answer': 'Aligning the camera at eye level ensures stable gaze alignment and posture, projecting professional engagement while allowing visual evaluation engines to measure eye alignment accurately.',
                'common_mistake': 'Looking down at a second monitor continuously while answering.',
                'practical_tip': 'Place the video call window directly below your webcam so looking at the interviewer aligns with the camera lens.',
                'practice_question': 'What is the recommended camera placement for online AI interviews?',
                'practice_options_json': [
                    'Far below your desk pointing upward.',
                    'Directly at eye level in line with your screen.',
                    'Behind your chair.',
                    'Off to the side facing the wall.'
                ],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Stress & Interview Pressure',
        'slug': 'stress-interview-pressure',
        'icon': 'fa-heart-pulse',
        'category_type': 'stress',
        'order': 12,
        'description': 'Managing unexpected pressure using the PAUSE-THINK-ANSWER composure framework.',
        'topics': [
            {
                'title': 'Managing Pressure: The 6-Step Composure Framework',
                'slug': '6-step-composure-framework',
                'difficulty': 'Intermediate',
                'summary': 'PAUSE -> UNDERSTAND -> THINK -> ANSWER -> EXAMPLE -> CONCLUDE.',
                'explanation': 'When encountering high-pressure or rapid questions, follow this step-by-step mental checklist:\n1. PAUSE: Take a deep breath.\n2. UNDERSTAND: Confirm the question requirement.\n3. THINK: Formulate 2 key points.\n4. ANSWER: State your primary thesis clearly.\n5. EXAMPLE: Back it up with a practical example.\n6. CONCLUDE: Summarize in one sentence.',
                'real_world_example': 'If asked a sudden rapid-fire follow-up, pause 1 second, state your answer, reference a project experience, and conclude smoothly.',
                'interview_question': 'How do you keep your technical composure when an interviewer challenges your design choice?',
                'sample_answer': 'I stay calm by pausing to listen completely. I thank the interviewer for the perspective, explain the rationale behind my initial design, and discuss trade-offs openly without becoming defensive.',
                'common_mistake': 'Becoming defensive or speaking rapidly when your answer is questioned.',
                'practical_tip': 'Note: Automated evaluation tools estimate visible behavioral indicators rather than diagnosing internal psychological stress.',
                'practice_question': 'What is the first step in the 6-step composure framework when receiving a difficult question?',
                'practice_options_json': ['Panic immediately', 'Pause and take a deep breath', 'Interrupt the interviewer', 'Change the topic'],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Interruption & Recovery',
        'slug': 'interruption-recovery',
        'icon': 'fa-bolt',
        'category_type': 'stress',
        'order': 13,
        'description': 'Handling interviewer interruptions, clarification challenges, and rapid follow-ups.',
        'topics': [
            {
                'title': 'Handling AI & Human Interviewer Interruptions',
                'slug': 'handling-interruptions',
                'difficulty': 'Intermediate',
                'summary': 'Acknowledge the interruption prompt gracefully and re-stabilize your train of thought.',
                'explanation': 'Interviewers interrupt for several reasons: to check technical depth, push for concise answers, or test how you recover under pressure. When interrupted:\n1. Stop speaking immediately.\n2. Listen carefully to the new prompt.\n3. Acknowledge the question ("Good point...").\n4. Provide a direct, targeted answer.',
                'real_world_example': 'Interviewer: "You said your app is scalable. How would you prove that?"\nBAD: "I don\'t know. I just think it is."\nBETTER: "I would measure scalability using response latency under load testing, concurrent connection limits, and database query profiling."',
                'interview_question': 'How do you recover if an interviewer interrupts you mid-sentence?',
                'sample_answer': 'I pause immediately, listen to the new prompt without frustration, address their specific question directly, and seamlessly resume or conclude my overall point.',
                'common_mistake': 'Talking over the interviewer or showing visible annoyance when interrupted.',
                'practical_tip': 'Treat interruptions as an invitation to give a more focused, high-value answer.',
                'practice_question': 'What should a candidate do immediately when an interviewer interrupts?',
                'practice_options_json': [
                    'Keep talking louder to finish their sentence.',
                    'Stop speaking immediately and listen carefully.',
                    'Walk out of the interview room.',
                    'Pretend they did not hear the interruption.'
                ],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Project Preparation',
        'slug': 'project-preparation',
        'icon': 'fa-diagram-project',
        'category_type': 'project',
        'order': 14,
        'description': 'Structure, explain, and defend your academic and personal software projects.',
        'topics': [
            {
                'title': 'How to Explain Your Technical Project in 60 Seconds',
                'slug': 'explain-project-60-seconds',
                'difficulty': 'Intermediate',
                'summary': 'Master the 5-point project pitch: Problem, Architecture, Tech Stack, Your Role, Result.',
                'explanation': 'Explain projects using a structured formula:\n1. Problem Statement: What real-world issue does it solve?\n2. Proposed System & Architecture: Overview of system design.\n3. Tech Stack: Frontend, backend, database, APIs.\n4. Your Contribution: Exactly what code/modules YOU built.\n5. Result & Metrics: Quantifiable outcome or key learning.',
                'real_world_example': 'Problem: Students struggle with interview stress. Solution: AI Interview Stress Analyzer built with Django, Web Speech API, and NLP heuristics where I personally implemented speech evaluation and stress metrics.',
                'interview_question': 'Walk me through your key software engineering project.',
                'sample_answer': 'I developed an AI-based Interview Stress Analyzer to help candidates prepare for placement rounds. Built using Django, SQL, and Web Speech APIs, the system evaluates candidate response relevance, speaking pacing, and stress indicators. I personally designed the database schema and backend API integration, improving response processing time by 30%.',
                'common_mistake': 'Saying "We built an app" without specifying what YOU personally coded.',
                'practical_tip': 'Always highlight YOUR specific module ownership: "My contribution was designing the REST APIs and database ORM layers."',
                'practice_question': 'Which element is most important when explaining a team project to a recruiter?',
                'practice_options_json': [
                    'Highlighting what other team members failed to do.',
                    'Clearly articulating your specific individual contribution.',
                    'Listing every single CSS color code used.',
                    'Ignoring the technologies used.'
                ],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Resume Preparation',
        'slug': 'resume-preparation',
        'icon': 'fa-file-invoice',
        'category_type': 'resume',
        'order': 15,
        'description': 'ATS formatting, highlighting key skills, and aligning your resume with interview rounds.',
        'topics': [
            {
                'title': 'Building an ATS-Friendly Technical Resume',
                'slug': 'ats-friendly-resume',
                'difficulty': 'Beginner',
                'summary': 'Format sections cleanly so Applicant Tracking Systems can parse your skills accurately.',
                'explanation': 'ATS parsers scan resumes for key domain terms (e.g. Python, SQL, REST API, Git). Use standard headings (Education, Technical Skills, Projects, Experience), avoid multi-column tables or image graphics, and list specific technologies under project bullet points.',
                'real_world_example': 'Under a project listing, include bullet points with action verbs: "Developed RESTful endpoints in Django ORM handling 500+ daily queries."',
                'interview_question': 'How do you ensure your resume accurately reflects your technical skills for recruiters?',
                'sample_answer': 'I structure my resume with standard ATS-friendly headings, categorize skills by domain (Languages, Frameworks, Databases, Tools), and back up every skill listed with measurable project achievements.',
                'common_mistake': 'Listing skills on your resume that you cannot explain or answer questions about during an interview.',
                'practical_tip': 'Rule of thumb: If it is on your resume, expect a deep-dive interview question about it.',
                'practice_question': 'What type of formatting should be avoided in ATS-friendly resumes?',
                'practice_options_json': [
                    'Standard text headings.',
                    'Complex multi-column graphics and image text.',
                    'Bullet points with technical keywords.',
                    'Clean single-column layouts.'
                ],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Coding Practice',
        'slug': 'coding-practice',
        'icon': 'fa-terminal',
        'category_type': 'coding',
        'order': 16,
        'description': 'Solve core placement coding questions with hints, solutions, and complexity analysis.',
        'topics': [
            {
                'title': 'Palindrome String Checker',
                'slug': 'palindrome-string-checker',
                'difficulty': 'Beginner',
                'summary': 'Determine if a given string reads the same backward as forward.',
                'explanation': 'A string is a palindrome if it equals its reverse after removing non-alphanumeric characters and converting to lowercase. You can solve it using two pointers (left and right) moving toward the center.',
                'real_world_example': '"racecar" is a palindrome. "hello" is not.',
                'interview_question': 'Write an efficient Python function to check if a string is a palindrome ignoring non-alphanumeric characters.',
                'sample_answer': 'I would clean the string using character checks or regex, then compare characters using two pointers from opposite ends in O(N) time and O(1) auxiliary space.',
                'common_mistake': 'Creating full reversed string copies in memory when O(1) space two-pointer approach is possible.',
                'practical_tip': 'Mention both two-pointer approach (O(1) space) and slice approach (`s == s[::-1]`).',
                'practice_question': 'What is the time complexity of checking a palindrome string of length N using two pointers?',
                'practice_options_json': ['O(N^2)', 'O(N)', 'O(1)', 'O(N log N)'],
                'correct_option_index': 1,
                'is_coding': True,
                'example_input': '"A man, a plan, a canal: Panama"',
                'example_output': 'True',
                'time_complexity': 'O(N)',
                'space_complexity': 'O(1)',
                'code_initial': 'def is_palindrome(s: str) -> bool:\n    # Write your solution here\n    pass',
                'code_hint': 'Use two pointers `left = 0` and `right = len(s) - 1`. Skip non-alphanumeric characters using `s[left].isalnum()`. Compare lowercases.',
                'code_solution': 'def is_palindrome(s: str) -> bool:\n    left, right = 0, len(s) - 1\n    while left < right:\n        while left < right and not s[left].isalnum():\n            left += 1\n        while left < right and not s[right].isalnum():\n            right -= 1\n        if s[left].lower() != s[right].lower():\n            return False\n        left += 1\n        right -= 1\n    return True'
            },
            {
                'title': 'Two Sum Target Problem',
                'slug': 'two-sum-target-problem',
                'difficulty': 'Intermediate',
                'summary': 'Find indices of two numbers in an array that add up to a target value.',
                'explanation': 'Given an array of integers `nums` and a target integer `target`, return indices of the two numbers such that they add up to `target`. Using a hash map allows looking up complementary values (`target - num`) in O(1) time.',
                'real_world_example': 'Finding two item prices in a database that total exactly \$100.',
                'interview_question': 'How does a Hash Map reduce Two Sum time complexity from O(N^2) to O(N)?',
                'sample_answer': 'A hash map stores previously seen numbers and their indices. For each element `x`, we check if `target - x` exists in the hash map. Hash map lookup is O(1) on average, resulting in single-pass linear O(N) execution.',
                'common_mistake': 'Using nested loops resulting in slow O(N^2) complexity.',
                'practical_tip': 'Always discuss the time-space tradeoff: Hash map trades O(N) space for O(N) time efficiency.',
                'practice_question': 'What is the optimal average time complexity for solving Two Sum using a Hash Map?',
                'practice_options_json': ['O(N^2)', 'O(N)', 'O(N log N)', 'O(1)'],
                'correct_option_index': 1,
                'is_coding': True,
                'example_input': 'nums = [2, 7, 11, 15], target = 9',
                'example_output': '[0, 1]',
                'time_complexity': 'O(N)',
                'space_complexity': 'O(N)',
                'code_initial': 'def two_sum(nums: list, target: int) -> list:\n    # Write your solution here\n    pass',
                'code_hint': 'Maintain a dictionary `seen = {}`. For index `i` and value `num`, check if `target - num` is in `seen`. If so, return `[seen[target - num], i]`. Else add `seen[num] = i`.',
                'code_solution': 'def two_sum(nums: list, target: int) -> list:\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i\n    return []'
            }
        ]
    },
    {
        'name': 'Common Interview Mistakes',
        'slug': 'common-interview-mistakes',
        'icon': 'fa-triangle-exclamation',
        'category_type': 'general',
        'order': 17,
        'description': 'Avoid classic pitfalls that derail candidate performance during placement rounds.',
        'topics': [
            {
                'title': 'Top 10 Placement Interview Mistakes & How to Avoid Them',
                'slug': 'top-10-interview-mistakes',
                'difficulty': 'Beginner',
                'summary': 'Recognize and fix common errors like memorizing code, vague answers, and ignoring questions.',
                'explanation': 'Common pitfalls include:\n1. Memorizing solutions without understanding fundamentals.\n2. Giving one-word answers ("Yes", "No", "I don\'t know").\n3. Talking continuously without checking if the interviewer understands.\n4. Pretending to know technologies listed on your resume that you haven\'t used.\n5. Neglecting to ask meaningful questions at the end.',
                'real_world_example': 'A candidate lists "Kubernetes" on their resume after watching a 10-minute video, but fails when asked about pod deployment manifest structure.',
                'interview_question': 'What is the biggest mistake candidates make when explaining code during a technical interview?',
                'sample_answer': 'The biggest mistake is writing code silently without explaining their thought process out loud. Interviewers care as much about your problem-solving logic and communication as they do about syntax correctness.',
                'common_mistake': 'Coding in total silence during a technical interview.',
                'practical_tip': 'Think out loud! Explain your initial thoughts, trade-offs, and edge cases as you write code.',
                'practice_question': 'Why should a candidate avoid coding in total silence during a technical interview?',
                'practice_options_json': [
                    'Because silent coding is forbidden by programming languages.',
                    'Because the interviewer needs to evaluate your problem-solving process and communication.',
                    'Because typing makes too much noise.',
                    'Because computers cannot run silent code.'
                ],
                'correct_option_index': 1
            }
        ]
    },
    {
        'name': 'Personalized Learning',
        'slug': 'personalized-learning',
        'icon': 'fa-wand-magic-sparkles',
        'category_type': 'general',
        'order': 18,
        'description': 'AI-driven custom recommendations based on your recent interview analytics and resume profile.',
        'topics': [
            {
                'title': 'AI Interview Analytics & Custom Improvement Roadmap',
                'slug': 'ai-analytics-improvement-roadmap',
                'difficulty': 'Intermediate',
                'summary': 'Turn your score breakdowns and feedback indicators into an actionable preparation path.',
                'explanation': 'The AI Interview analyzer tracks performance metrics across Communication, Relevance, Stress Handling, Cognitive Reasoning, and Technical Explanations. Use low sub-scores to target specific Learning Center topics for maximum placement impact.',
                'real_world_example': 'If your report shows 45% on Filler Word Control and 85% on Technical Quality, focus 70% of your prep on Communication & Answer Structuring modules.',
                'interview_question': 'How do you turn post-interview feedback into structured technical improvement?',
                'sample_answer': 'I review metric breakdowns objectively, identify specific weak dimensions (such as response relevance or composure under rapid follow-up), and complete focused practice modules before retaking mock interview simulations.',
                'common_mistake': 'Ignoring evaluation feedback and repeating the same interview mistakes.',
                'practical_tip': 'Retake an AI Interview session after completing recommended Learning Center topics to measure score improvement.',
                'practice_question': 'What is the purpose of analyzing weak score dimensions after an AI interview session?',
                'practice_options_json': [
                    'To discourage candidates from trying again.',
                    'To pinpoint specific skills to practice in the Learning Center.',
                    'To delete your profile history.',
                    'To lock all coding challenges.'
                ],
                'correct_option_index': 1
            }
        ]
    }
]

def seed_learning_data():
    """Seeds the database with learning categories and topics if empty."""
    from interview.models import LearningCategory, LearningTopic
    
    for cat_data in LEARNING_DATA:
        topics_data = cat_data.pop('topics', [])
        category, created = LearningCategory.objects.get_or_create(
            slug=cat_data['slug'],
            defaults=cat_data
        )
        cat_data['topics'] = topics_data # restore dictionary
        
        for idx, top_data in enumerate(topics_data):
            LearningTopic.objects.get_or_create(
                category=category,
                slug=top_data['slug'],
                defaults={
                    'title': top_data['title'],
                    'difficulty': top_data.get('difficulty', 'Beginner'),
                    'order': idx + 1,
                    'summary': top_data.get('summary', ''),
                    'explanation': top_data.get('explanation', ''),
                    'real_world_example': top_data.get('real_world_example', ''),
                    'interview_question': top_data.get('interview_question', ''),
                    'sample_answer': top_data.get('sample_answer', ''),
                    'common_mistake': top_data.get('common_mistake', ''),
                    'practical_tip': top_data.get('practical_tip', ''),
                    'practice_question': top_data.get('practice_question', ''),
                    'practice_options_json': top_data.get('practice_options_json', []),
                    'correct_option_index': top_data.get('correct_option_index', 0),
                    'is_coding': top_data.get('is_coding', False),
                    'code_initial': top_data.get('code_initial', ''),
                    'code_hint': top_data.get('code_hint', ''),
                    'code_solution': top_data.get('code_solution', ''),
                    'example_input': top_data.get('example_input', ''),
                    'example_output': top_data.get('example_output', ''),
                    'time_complexity': top_data.get('time_complexity', ''),
                    'space_complexity': top_data.get('space_complexity', '')
                }
            )
