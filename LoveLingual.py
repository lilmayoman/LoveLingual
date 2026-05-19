import tkinter as tk
from tkinter import font

class LoveLanguageQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Love Language Questionnaire")
        self.root.geometry("600x400")
        self.root.config(bg="#1a1a1a")
        
        # Configure styles
        self.title_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.question_font = font.Font(family="Helvetica", size=11)
        self.button_font = font.Font(family="Helvetica", size=10)
        
        # Love languages
        self.love_languages = [
            "Words of Affirmation",
            "Acts of Service",
            "Receiving Gifts",
            "Quality Time",
            "Physical Touch"
        ]
        
        # Questions: (question_text, option1_text, option1_language, option2_text, option2_language)
        self.questions = [
            ("What would make your day?",
             "Your partner brings home your favorite snack without you asking", "Acts of Service",
             "Your partner hugs you from behind while you're cooking", "Physical Touch"),
            
            ("When you're having a tough day, what helps most?",
             "Your partner puts their hand on your shoulder and listens", "Physical Touch",
             "Your partner tells you exactly why they think you're amazing", "Words of Affirmation"),
            
            ("What's the perfect Sunday?",
             "A long hike or adventure together with no distractions", "Quality Time",
             "Your partner leaves little love notes around the house for you to find", "Words of Affirmation"),
            
            ("How does your partner show they care most?",
             "By remembering small details you mentioned weeks ago and surprising you with relevant gifts", "Receiving Gifts",
             "By taking care of the chores so you can relax", "Acts of Service"),
            
            ("What makes you feel truly connected?",
             "Holding hands, cuddling, or other physical affection", "Physical Touch",
             "Deep conversations where they really understand you", "Quality Time"),
            
            ("Your ideal evening together includes...",
             "Sitting close together watching your favorite show", "Physical Touch",
             "Them telling you how much you mean to them", "Words of Affirmation"),
            
            ("When you accomplish something, what matters?",
             "Your partner gives you flowers or a special gift to celebrate", "Receiving Gifts",
             "Your partner says they're proud of you and tells everyone", "Words of Affirmation"),
            
            ("What would make you feel most appreciated?",
             "Your partner preparing your favorite meal or fixing something you've been worried about", "Acts of Service",
             "A full day together with their complete attention", "Quality Time"),
            
            ("Which touches your heart more?",
             "Finding out they ran errands for you without being asked", "Acts of Service",
             "Them playing with your hair or giving you a massage", "Physical Touch"),
            
            ("What's most romantic to you?",
             "A thoughtfully wrapped present chosen just for you", "Receiving Gifts",
             "Uninterrupted time together talking about your dreams", "Quality Time"),
            
            ("After a long day at work, you want...",
             "Your partner to rub your shoulders and be physically close", "Physical Touch",
             "Your partner to tell you that you handled everything beautifully", "Words of Affirmation"),
            
            ("What makes you feel like they truly understand you?",
             "They remember the small things you mentioned in passing", "Words of Affirmation",
             "They make time to sit down and really listen to you", "Quality Time"),
            
            ("You'd rather they...",
             "Book a surprise getaway adventure for you two", "Quality Time",
             "Surprise you with a gift they know you've been wanting", "Receiving Gifts"),
            
            ("What's the sweetest gesture?",
             "Them noticing you're tired and taking over your responsibilities for the day", "Acts of Service",
             "A loving text in the middle of the day saying they're thinking of you", "Words of Affirmation"),
            
            ("In moments of intimacy, what matters most to you?",
             "Hugging, kissing, and feeling their physical presence", "Physical Touch",
             "Having their full attention and being the center of their world", "Quality Time"),
            
            ("When you're sick or struggling, your partner would best help by...",
             "Preparing your favorite comfort food and taking care of household tasks", "Acts of Service",
             "Bringing you a thoughtful care package with small gifts inside", "Receiving Gifts"),
            
            ("What's a dealbreaker for you?",
             "Them never taking the initiative to spend alone time with you", "Quality Time",
             "Them not acknowledging your efforts or saying 'thank you'", "Words of Affirmation"),
            
            ("When you need comfort, you prefer...",
             "Them holding you close without needing to say anything", "Physical Touch",
             "Them stepping in to handle problems so you don't have to worry", "Acts of Service"),
            
            ("Your partner would win you over by...",
             "Planning a special date night tailored perfectly to your interests", "Quality Time",
             "Presenting you with something they picked out especially for you", "Receiving Gifts"),
            
            ("Which moment feels most intimate?",
             "When they compliment you on who you are, not just what you do", "Words of Affirmation",
             "When they reach for your hand or pull you close without thinking", "Physical Touch")
        ]
        
        self.current_question = 0
        self.scores = {language: 0 for language in self.love_languages}
        self.setup_question_screen()
    
    def setup_question_screen(self):
        """Display the current question with two options"""
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Progress indicator
        progress_label = tk.Label(
            self.root,
            text=f"Question {self.current_question + 1} of {len(self.questions)}",
            font=font.Font(family="Helvetica", size=10),
            bg="#1a1a1a",
            fg="#888888"
        )
        progress_label.pack(pady=10)
        
        # Question text
        question_data = self.questions[self.current_question]
        question_text = question_data[0]
        
        question_label = tk.Label(
            self.root,
            text=question_text,
            font=self.title_font,
            bg="#1a1a1a",
            fg="#e0e0e0",
            wraplength=550
        )
        question_label.pack(pady=20)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg="#1a1a1a")
        button_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        # Option 1 (Blue Portal color)
        option1_text = question_data[1]
        option1_language = question_data[2]
        option1_button = tk.Button(
            button_frame,
            text=option1_text,
            font=self.button_font,
            bg="#1E3A8A",
            fg="white",
            activebackground="#2D5BB5",
            activeforeground="white",
            wraplength=250,
            justify=tk.CENTER,
            pady=20,
            command=lambda: self.handle_answer(option1_language)
        )
        option1_button.pack(side=tk.LEFT, padx=15, fill=tk.BOTH, expand=True)
        
        # Option 2 (Orange Portal color)
        option2_text = question_data[3]
        option2_language = question_data[4]
        option2_button = tk.Button(
            button_frame,
            text=option2_text,
            font=self.button_font,
            bg="#92400E",
            fg="white",
            activebackground="#B85C11",
            activeforeground="white",
            wraplength=250,
            justify=tk.CENTER,
            pady=20,
            command=lambda: self.handle_answer(option2_language)
        )
        option2_button.pack(side=tk.LEFT, padx=15, fill=tk.BOTH, expand=True)
    
    def handle_answer(self, language):
        """Handle the user's answer"""
        self.scores[language] += 1
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.setup_question_screen()
        else:
            self.show_results()
    
    def show_results(self):
        """Display the results ranked by percentage"""
        # Resize window for results
        self.root.geometry("600x750")
        
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Results title
        results_title = tk.Label(
            self.root,
            text="Your Love Language Profile",
            font=self.title_font,
            bg="#1a1a1a",
            fg="#FF6B9D"
        )
        results_title.pack(pady=20)
        
        # Calculate percentages and sort
        total_score = sum(self.scores.values())
        percentages = {lang: (self.scores[lang] / total_score * 100) for lang in self.love_languages}
        sorted_languages = sorted(percentages.items(), key=lambda x: x[1], reverse=True)
        
        # Display results
        results_frame = tk.Frame(self.root, bg="#1a1a1a")
        results_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        for rank, (language, percentage) in enumerate(sorted_languages, 1):
            # Language and rank
            label_text = f"{rank}. {language}"
            lang_label = tk.Label(
                results_frame,
                text=label_text,
                font=font.Font(family="Helvetica", size=11, weight="bold"),
                bg="#1a1a1a",
                fg="#e0e0e0",
                justify=tk.LEFT
            )
            lang_label.pack(anchor="w", pady=5)
            
            # Percentage bar
            bar_frame = tk.Frame(results_frame, bg="#333333", height=25)
            bar_frame.pack(fill=tk.X, pady=2)
            
            # Color gradient based on rank - using Portal-inspired colors
            colors = ["#FF6B9D", "#FF8FAB", "#FF9DB8", "#2E5FD1", "#6B93D6"]
            color = colors[min(rank - 1, len(colors) - 1)]
            
            # Fill bar
            fill_width = int(300 * percentage / 100)
            fill_bar = tk.Frame(bar_frame, bg=color, height=25, width=fill_width)
            fill_bar.pack(side=tk.LEFT, fill=tk.Y)
            
            # Percentage text
            percent_label = tk.Label(
                results_frame,
                text=f"{percentage:.1f}%",
                font=font.Font(family="Helvetica", size=10),
                bg="#1a1a1a",
                fg="#888888"
            )
            percent_label.pack(anchor="e", pady=2)
        
        # Close button
        close_button = tk.Button(
            self.root,
            text="Close",
            font=self.button_font,
            bg="#333333",
            fg="white",
            activebackground="#444444",
            activeforeground="white",
            width=15,
            command=self.root.quit
        )
        close_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    quiz = LoveLanguageQuiz(root)
    root.mainloop()
