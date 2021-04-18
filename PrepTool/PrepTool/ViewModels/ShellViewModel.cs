using Caliburn.Micro;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using PrepTool.Models;

namespace PrepTool.ViewModels
{
    public class ShellViewModel : Conductor<object>
    {
        private bool _showAnswer=false;

        public bool ShowAnswer
        {
            get
            {
                return _showAnswer;
            }
            set
            {
                if (_showAnswer)
                {
                    _showAnswer = false;
                }
                else
                {
                    _showAnswer = true;
                }
                NotifyOfPropertyChange(() => ShowAnswer);
            }
        }


        public void CheckAnswer()
        {
            ShowAnswer = true;
            return;
        }

        public void NextQuestion()
        {
            // update the path to uri
            return;
        }
        
    }
}
